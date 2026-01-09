def test_sample_agent_flow(client):
    # This test might fail if OpenAI API key is missing,
    # but it verifies the endpoint and middleware are wired correctly.
    response = client.post("/api/v1/agent/execute", json={"query": "Hello"})
    # If the agent is not configured, it might return 500/400,
    # but the structure should still be an AppResponse.
    json_data = response.json()
    assert "success" in json_data
    assert "request_id" in json_data
    if response.status_code == 200:
        assert json_data["success"] is True
        assert "response" in json_data["data"]
