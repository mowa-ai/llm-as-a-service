from laas import api_models, engine


def test_preprocess_message():
    engine_input = api_models.EngineInput(
        history=[
            api_models.HistoryRecord(role=api_models.MessageType.system, content="Dummy system message"),
            api_models.HistoryRecord(role=api_models.MessageType.assistant, content="Dummy assistant message"),
            api_models.HistoryRecord(role=api_models.MessageType.user, content="Dummy user message"),
            api_models.HistoryRecord(role=api_models.MessageType.assistant, content="Second dummy assistant message"),
        ]
    )
    expected_output = [
        {"role": "system", "content": "Dummy system message"},
        {"role": "assistant", "content": "Dummy assistant message"},
        {"role": "user", "content": "Dummy user message"},
        {"role": "assistant", "content": "Second dummy assistant message"},
    ]

    output = engine.preprocess_message(engine_input)
    assert output == expected_output
