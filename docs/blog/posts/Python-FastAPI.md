---
layout: post
title: "Fast API"
author: "Ray"
header-style: text
tags:
    - python
    - FastAPI
date: 2023-12-19
---

# install

## github setup, it depends rust and might need this:

### ((64c9b153-f65d-4260-abe8-0b04a23afdb3))

### `cargo install --locked maturin` well seems this need to install separately for windows

### #+BEGIN~SRC~ shell

pacman -S mingw-w64-clang-x86~64~-python-installer
mingw-w64-clang-x86~64~-python-wheel \\
mingw-w64-clang-x86~64~-python-setuptools-rust
mingw-w64-clang-x86~64~-python-build

python -m venv --system-site-packages venv3

```{=org}
#+END_SRC
```
### `pip install "fastapi[all]"`

\* \*
