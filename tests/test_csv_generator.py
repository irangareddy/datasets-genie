"""Test CSV Generator"""
import os
import csv
import sys
from io import StringIO
import pytest

from datasets_genie.csv_generator import generate_csv, generate_data, data_stream

FILE_LOCATION = "./tests"
FILE_NAME = "test_file.csv"


@pytest.fixture(scope="session", autouse=True)
def setup():
    """test setup"""
    if not os.path.exists(FILE_LOCATION):
        os.makedirs(FILE_LOCATION)


@pytest.fixture(autouse=True)
def teardown():
    """test_teardown"""
    if os.path.exists(f"{FILE_LOCATION}/{FILE_NAME}"):
        os.remove(f"{FILE_LOCATION}/{FILE_NAME}")


@pytest.mark.parametrize("rows, columns", [(10, 5), (100, 20), (1000, 100)])
def test_generate_data(rows, columns):
    """generate_data"""
    data = generate_data(rows, columns)
    assert len(data) == rows + 1  # account for header row
    assert len(data[0]) == columns
    for row in data[1:]:
        assert len(row) == columns


@pytest.mark.parametrize(
    "rows,columns",
    [
        (5, 3),
        (10, 4),
    ],
)
def test_generate_csv_creates_csv_file(rows, columns):
    """generate_csv_creates_csv_file"""
    generate_csv(
        rows=rows, columns=columns, file_location=FILE_LOCATION, file_name=FILE_NAME
    )
    assert os.path.exists(f"{FILE_LOCATION}/{FILE_NAME}")


@pytest.mark.parametrize(
    "rows,expected_rows",
    [
        (5, 6),
        (10, 11),
    ],
)
def test_generate_csv_correct_number_of_rows(rows, expected_rows):
    """generate_csv_correct_number_of_rows"""
    generate_csv(rows=rows, columns=3, file_location=FILE_LOCATION, file_name=FILE_NAME)
    with open(f"{FILE_LOCATION}/{FILE_NAME}", "r") as csvfile:
        reader = csv.reader(csvfile)
        assert len(list(reader)) == expected_rows  # 1 for keys and rows for data rows


@pytest.mark.parametrize(
    "columns",
    [
        3,
        4,
        5,
    ],
)
def test_generate_csv_correct_number_of_columns(columns):
    """generate_csv_correct_number_of_columns"""
    generate_csv(
        rows=5, columns=columns, file_location=FILE_LOCATION, file_name=FILE_NAME
    )
    with open(f"{FILE_LOCATION}/{FILE_NAME}", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            assert len(row) == columns


def test_generate_csv_preview_option_outputs_to_console():
    """generate_csv_preview_option_outputs_to_console"""
    captured_output = StringIO()
    sys.stdout = captured_output
    generate_csv(rows=5, columns=3, preview=True)
    sys.stdout = sys.stdout
    assert captured_output.getvalue() != ""


@pytest.mark.parametrize(
    "rows,expected_output_rows",
    [
        (5, 5),
        (10, 5),
    ],
)
def test_generate_csv_preview_option_outputs_only_5_rows(rows, expected_output_rows):
    """generate_csv_preview_option_outputs_only_5_rows"""
    captured_output = StringIO()
    sys.stdout = captured_output
    generate_csv(rows=rows, columns=3, preview=True)
    sys.stdout = sys.stdout
    output = captured_output.getvalue()
    assert output.count("\n") == expected_output_rows  # 5 rows were printed


def test_data_stream():
    """test data stream"""
    data = [1, 2, 3, 4, 5]
    stream = data_stream(data)
    for i, item in enumerate(stream):
        assert item == data[i]
