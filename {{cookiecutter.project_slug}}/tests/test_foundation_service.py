from app.services.foundation_service import LocalMockFoundationDataService


def test_foundation_service_returns_mock_record() -> None:
    records = LocalMockFoundationDataService().query("AAPL")
    assert records
    assert records[0].source == "local-mock"


def test_foundation_service_returns_empty_for_blank_identifier() -> None:
    assert LocalMockFoundationDataService().query("   ") == []
