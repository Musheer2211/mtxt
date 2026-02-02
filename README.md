# Frequency-Based Prefix Encoding

A simple frequency-based compression scheme using variable-length, prefix-free bit encodings.

## Encoding Rule

Symbols are encoded based on descending frequency:

- Most frequent: `1`
- Second most frequent: `01`
- Third most frequent: `001`
- Fourth most frequent: `0001`
- And so on...

Each code consists of zero or more `0`s followed by a terminating `1`.

## Overview

- Variable-length encoding
- Shorter codes for more frequent symbols
- Prefix-free and easy to decode
- Related to unary coding and Huffman-style ideas

## Notes

This method favors simplicity and determinism over optimal compression efficiency and works best with highly skewed symbol frequencies.
