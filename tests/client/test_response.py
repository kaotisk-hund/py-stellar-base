from stellar_sdk.client.response import Response


class TestResponse:
    def test_json(self):
        resp = Response(
            status_code=200,
            text='{"a": "b", "c": "d"}',
            headers={"User-Agent": "Stellar"},
            url="https://httpbin.overcat.me",
        )
        assert resp.json() == {"a": "b", "c": "d"}

    def test_equal(self):
        resp1 = Response(
            status_code=200,
            text="{'a': 'b', 'c': 'd'}",
            headers={"User-Agent": "Stellar"},
            url="https://httpbin.overcat.me",
        )

        resp2 = Response(
            status_code=200,
            text="{'a': 'b', 'c': 'd'}",
            headers={"User-Agent": "Stellar"},
            url="https://httpbin.overcat.me",
        )

        resp3 = Response(
            status_code=404,
            text="{'a': 'b', 'c': 'd'}",
            headers={"User-Agent": "Stellar"},
            url="https://httpbin.overcat.me",
        )

        resp4 = "BAD TYPE"

        assert resp1 == resp2 != resp3 != resp4
