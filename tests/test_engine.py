from laas import engine, api_models


def test_preprocess_message():
    engine_input = api_models.EngineInput(
        history=[
            api_models.HistoryRecord(type=api_models.MessageType.system, text="Dummy system message"),
            api_models.HistoryRecord(type=api_models.MessageType.assistant, text="Dummy assistant message"),
            api_models.HistoryRecord(type=api_models.MessageType.user, text="Dummy user message"),
            api_models.HistoryRecord(type=api_models.MessageType.assistant, text="Second dummy assistant message"),
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
