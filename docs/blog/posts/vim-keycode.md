---
layout: post
title: "keycode in terminal for vim&neovim "
subtitle: ["Map special keys (e.g <s-f1>) in vim & nvim in terminal", "vi/kitty/zsh shift+fn 配置"]
author: "Ray"
header-style: text
tags:
  - vim, kitty neovim
date: 2020-06-10
---


# How keys was defined in terminal

This had never been a issue until I give up vimr and use kitty + neovim. I found that my ``<S-Fn>`` no longer works.

Well, do panic, use `infocmp` or `keybind` or `keycode` to find out how the key is defined (also can use `cat` or `sed
-n -l`).
For kitty `<S-F1>` key code is `^[[1;2P` . Here `^[` means `<Esc>` or `\E`

vim and neovim handle key code slight different.

for neovim, S-Fn was map to F(12+n) , e.g. S-f1 mapped to F13.
So you can do this:

```vim
    map <F13> <S-F1>
```
vim is slightly different. `:help keycode`

```vim
    set <S-F1>=^[[1;2P
    map <Esc>[1;2P <S-F1>
```

So put it all together
``` vim
if !has("gui_running")
  if !has('nvim')
    set <S-F1>=^[[1;2P
    map <Esc>[1;2P <S-F1>
    set <S-F2>=^[[1;2Q
    map <Esc>[1;2Q <S-F2>
    set <S-F3>=^[[1;2R
    map <Esc>[1;2R <S-F3>
  else
    map <F13> <S-F1>
    map <F14> <S-F4>
    map <F15> <S-F5>
    map <F16> <S-F6>
  endif
endif

```
