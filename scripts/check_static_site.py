#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    target = ROOT / path
    if not target.exists():
        raise AssertionError(f"missing {path}")
    return target.read_text(encoding="utf-8")


def assert_contains(text, needle, label):
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


def assert_not_contains(text, needle, label):
    if needle in text:
        raise AssertionError(f"{label}: unexpectedly contains {needle!r}")


def assert_before(text, first, second, label):
    first_index = text.find(first)
    second_index = text.find(second)
    if first_index == -1 or second_index == -1:
        raise AssertionError(f"{label}: could not find ordered markers")
    if first_index >= second_index:
        raise AssertionError(f"{label}: {first!r} should appear before {second!r}")


def main():
    if not (ROOT / ".nojekyll").exists():
        raise AssertionError("missing .nojekyll")

    index = read("index.html")
    day6 = read("docs/Day 6 - Array 数组3.html")

    assert_contains(index, 'class="preview-layout"', "home")
    assert_contains(index, 'class="preview-nav"', "home")
    assert_contains(index, "28 天速通 LeetCode", "home")
    assert_contains(index, "docs/Day 6 - Array 数组3.html", "home")
    assert_not_contains(index, "just-the-docs-default.css", "home")
    assert_not_contains(index, 'class="site-nav"', "home")
    assert_before(index, "Day 2 - Linked List 链表2", "Day 10 - BST 二叉树3", "home nav order")

    assert_contains(day6, 'class="preview-layout"', "day6")
    assert_contains(day6, 'class="preview-nav"', "day6")
    assert_contains(day6, 'class="active"', "day6")
    assert_contains(day6, "Day 6 - Array 数组3", "day6")
    assert_contains(day6, "fourSum", "day6")
    assert_contains(day6, 'class="codehilite"', "day6")
    assert_contains(day6, 'class="kd"', "day6")
    assert_not_contains(day6, "just-the-docs-default.css", "day6")
    assert_not_contains(day6, 'class="site-nav"', "day6")


if __name__ == "__main__":
    main()
