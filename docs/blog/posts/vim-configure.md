---
layout: post
title: "Sharing my dotfiles(vim/kitty/zsh configuration)"
subtitle: ["vi/kitty/zsh configuration I recommend", "vi/kitty/zsh 配置"]
author: "Ray"
header-style: text
tags:
  - vim, kitty
date: 2020-06-06
---


# vim as a programming ide

I used to use slickedit, qt-creator, idea (webstorm, goland), vscode, but I am back to vi now. Thanks for `Plug` I do
not need to configure my setup everytime....... I am still using sublime edit(as a notepad)

vimr is one of the best nvim-gui. But it does not in active development in last 3 months(It is hard for a one developer
project), some of the crash durning coding is annoying. I only use nvim/vim + kitty now.

* nvim+kitty configured with pop menu:

    ![vim_ide with nvim+kitty](https://raw.githubusercontent.com/ray-x/dotfiles/master/img/menu.jpg)

* nvim clap preview:

    ![vim_ide with nvim+kitty](https://raw.githubusercontent.com/ray-x/dotfiles/master/img/clap.jpg)

* nvim+kitty coc+ale:

    ![vim_ide with nvim+kitty](https://raw.githubusercontent.com/ray-x/dotfiles/master/img/coc_float_errorcheck.jpg)


## Vim Plugins

I used following plugin a lots

* ``Plug``

   Plugin management tool

* vim-clap

   Best plugin for search anything. I used it to replace fzf, leaderF, leaderP, NerdTree, Ag/Ack/Rg, yank(ring), project management. undolist and many more

* coc.nvim

   I disabled vim-go and turn to coc-go. Replace defx with coc-explorer, use coc-spell for spell check
   coc-snippet replaced my ultisnips. Also, there are coc for yml, json, prettier, python, rust, PHP (any language vs code
   supported)......

* ALE

  well, I am still using ALE and configure lots of lint tool with it.

* Programming support:

  YCM (used to be my favourite, only for C++ and python now), but I am using coc.nvim more offen now,
  vim-go(for go testing, highlight, gopls disabled),CompleteParameter, emmet-vim, tagbar/vista, polygot,
  and some language specific plugins (e.g html, js/ts, swift), ctags/gutentags, vim-less, govim(macvim only, with some cool AST)

* Debug:

  vimspector

* Theme, look&feel:

  onedark, eleline, devicons, startify, powerline, indentLine(with nerdfont),

* Color:

  nvim-colorizer.lua (display hex and color in highlight), rainbow, log-highlight, limelight, interestingwords

* Git:

  fugitive, gv, coc-git

* Format:

  tabular, coc-prettier(or, sometimes prettier), auto-pair

* Menu and tab:
  quickui(created a menu for the function/keybind I used less often. I can not rememeber all the commands and keybinds....)
  wintab: one of the best buffer management tool

* Tools: floatterm, coc-todolist

* Move and Edit:

  easymotion, multi-cursor (has ome bugs with auto-complete. check this: [You don’t need more than one cursor in vim](https://medium.com/@schtoeffel/you-don-t-need-more-than-one-cursor-in-vim-2c44117d51db)
), vim-anyfold (better folding)

## Shell

* OMZshell is good, iterm2 is popular, but I turned to zprezto(with powerlevel10) + kitty. It is cooool and faster, check this:

Some of the benfits of kitty:

* Fully GPU/OpenGL rendering

* Easy split/tabing

* Configurable font. You can configure multiple fonts for display. e.g. my configure:


```yml
font_family      FiraCode Retina
italic_font      InconsolataLGC Nerd Font Italic
bold_font        FiraCode Semibold
bold_italic_font InconsolataLGC Nerd Font BoldItalic

# Font size (in pts)
font_size        16.0


```

Why am I doing this:

* bold font is too heavy... semibold is less distracting

* Retina font is better than regular (I guess...)

* nerd font support

* Some font do not have italic (e.g. Cascadia)


nvim+kitty split view:

 ![vim_ide with nvim+kitty](https://raw.githubusercontent.com/ray-x/dotfiles/master/img/kitty.jpg)


[Check my repo](https://github.com/ray-x/dotfiles)
