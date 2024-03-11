---
layout: post
title: "nvim trick"
author: "Ray"
header-style: text
tags:
  - nvim
date: 2022-12-16
---

Some Neovim tricks

# [*nvim*]{.spurious-link target="nvim"} [*keymap*]{.spurious-link target="keymap"}

## \< C-Y \> scroll-up

## \<C-U\> scroll-down

## `H`, `M`, `L` go to high/middle/low it should move to first non empty line

## `d33|` `|` moves the cursor to the specified column in the current line

## Find replace

### `&` stands for the matched words

### press `*` and do `:%s//xxx/` the search is omitted and it is the current selected word

## Move around

### `+` `-` can also be used to move to `+` Move to first none empty char of next line

### `<CR>` can move to head of next line

## word and WORD

### **The difference between words and WORDS is that the former only include letters, digits and numbers**.

### word can be a sequences of spaces. do `dw` inside a sequence of space and see what you get. w, b, e, ge are word motions.

### `W` move on WORD boudnary. following are WORD `helloVimWord(){}`, `[1,2,3,4,5]` etc

## `i` `a`; there is also `I` and `A` insert at begin of line and end of line

## `Y` yank; it is same as `yy`; `P` past above

## `s` and `S` was remapped in hop/leap. `s` -\> `cl` `S` -\> cc

\*\*

## `X` delete char left of cursor (\<BS\> in norm mode)

## command range and `g / v` command

### `:.` current line

### `:%` entire file

### `$~last line
*** ~:12` line 12

### `:12,14s/import/export/g` replace from line 12 to 14

### `:.,.+12` from current line to current line + 12

### `:.,$` from current line to eof

### `:g/import/d` delete lines include `import`

### `:g!/import/d` delete lines do NOT include `import` it same as `v` command `:v/import/d`

## motion vs `/` command

### all motion can be replace with find `/` command. e.g `dft` can also be `d/t<cr>`

## delete

### `d0` delete to begin of line

### use `s` to delete

1.  `:%s/abc//<CR>`

2.  it can also write as `:%s/abc<CR>`

### `db` backward delete word

### `dvb` and `dve` delete `inclusive` ; `dvge`;

### `das` `dap`

### `dF*` search backward and delete

### with surround `di*` `ca*` `da*` etc

### `dh` delete 1 char to the left; `d3h` delete 3chars to the right

**\***

## #vim~g~

### `g0` go to 0; same as `gg`

### `ge` jump back end of word

### `g&` it similar to macro, a command in Vim that repeats the last substitution (`:s`) command on all lines in the file. It\'s equivalent to `:%s//~/g`, where `//` reuses the last search pattern, and `~` reuses the last replacement string.

### `gJ` join \[cnt\] lines `J`: join with remove indent, also works in visual mode

### `gq` format text

### wrap: `gj`, `gk` jump inside long lines , `g$`, `g^`

### `g<C-A>` in visual mode/range, increase number of each line based on fist value in range. e.g. `1 1 1 1` -\> `1 2 3 4`

### `gu|U` + text obj capitalization, e.g. `gu$` `guW`, `guu` whole line, `gU3w`, `gufk` (lowcase to letter k)

### \`g\~\` similar to `gu|U`

### `gv` re-select text

### `g&` apply the replace changes to full document. It is helpful when you need to replace in one line and check if replace is correct and apply to full text

**\***

## Search and replace

### `*%s/.$/&;/*` `.$` match a none empty line `&~is what was matched
*** ~:v/^$/s/$/;`

1.  `:v` inverse find `/^$` is empty line

2.  `/s/$/;` command of `v`; replace EOL to `;`

### `\ze`: `\ze` Zero-width ending split the search pattern into two, first half is match can be used later on, e.g. `end\ze(if|for)` match both `endif` and `endfor` but the matched pattern is `end` so `:s/\vend\ze(if|for)/&_/g` replace `endif` to `end_if`

## `put=range(1,10)` add 1\~10 to buffer

## `<C-R>=` e.g. `<C-R>=range(1,10)` use register with value of expression

## indentation

### `v>` indent current line to the right

### `>G` indent from current line the the end of file to the right

### `=G` remove indent from current to eof

### `>{` indent to right from begin of block to current line

### `=` in visual mode, indent current line (based on context)

### `>>` indent to the right with normal mode

## <https://www.vimgolf.com/challenges/596dd9ca448256000c000011>

## <https://www.vimgolf.com/challenges/5ba020f91abf2d000951055c>

# Fugutive diff merge

## reference `http://vimcasts.org/episodes/fugitive-vim-resolving-merge-conflicts-with-vimdiff/`

## `Gdiff` are used to merge diff conflicts. You can also use `Gvdiffsplit!` It opens

### left(the branch you used to work on, or local branch) . The buff is named as fugutive//2

### middle the current working file,

### right buffer which is the remote branch that you trying to merged into current branch (remote). the buffer named fugutive://3

### If the cursor in middle buffer, `diffget //2` get changes from left file and use `]c` to jump to next merge conflict. and use `diffupdate` to refresh file

### when done, use `only` to close other windows

### You can use `diffput 1` to put changes throught. in fugutive, `dp` default alias to `diffput 1`

### `Gwrite!`

# Diffview

## If git in merge status, `DiffViewOpen` will show the conflicts files

## `<Leader>co|ct|cb|ca` select Ours, Theirs, Base and All or `dx` choose none

\*\*
