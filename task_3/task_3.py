from typing import Any
from json import dump, load


def parse_json_to_dict(file_path: str) -> dict[Any, Any]:
    try:
        with open(file_path) as file_handler:
            json_data = load(file_handler)
            return json_data
    finally:
        file_handler.close()


def load_to_file(file_path: str, data: Any) -> None:
    try:
        with open(file_path, "w") as file_handler:
            dump(data, file_handler)
    finally:
        file_handler.close()


def format_values(values: list[dict[Any, Any]]) -> dict[int, str]:
    formatted_values = {
        x.get("id"): x.get("value")
        for x in values if x.get("id")
    }
    return formatted_values


def create_report(
    tests: list[dict[Any, Any]],
    values: dict[int, str],
) -> None:
    for obj in tests:
        if obj_values := obj.get("values"):
            create_report(obj_values, values)
        obj_id = obj.get("id")
        if obj_id in values:
            obj["value"] = values.get(obj_id)


def main(
    path_values: str,
    path_tests: str,
    path_report: str,
) -> None:
    values_obj = parse_json_to_dict(path_values)
    tests_obj = parse_json_to_dict(path_tests)
    values, tests = values_obj.get("values"), tests_obj.get("tests")
    values = format_values(values)
    create_report(tests, values)
    load_to_file(path_report, tests_obj)


if __name__ == '__main__':
    path_values = "values.json"
    path_tests = "tests.json"
    path_report = "report.json"
    main(path_values, path_tests, path_report)