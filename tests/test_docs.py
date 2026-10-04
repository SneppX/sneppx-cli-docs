from pathlib import Path

def test_docs_index_exists():
    docs = Path(__file__).parent.parent / "docs" / "index.md"
    assert docs.exists()
    assert "sneppx-train" in docs.read_text(encoding="utf-8")
