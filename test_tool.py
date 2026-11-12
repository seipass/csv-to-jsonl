from csv_to_jsonl import transform
def test_transform():
 assert transform([{"x":"a"}]) == '{"x": "a"}'
