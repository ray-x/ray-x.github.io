---
layout: post
title: "Replace fzf with vim-clap"
subtitle: ["swiss army knife for searching in vim", "vi-clap 简介与配置"]
author: "Ray"
header-style: text
tags:
  - vim, kitty neovim vim-clap
date: 2020-06-11
---


# vim-clap is a combination of fzf, ctrlp, leaderF, Ag/Ack, nerdtree(in some extends) ......

Check this:
![Clap](https://user-images.githubusercontent.com/8850248/73323347-24467380-4282-11ea-8dac-5ef5a1ee63bb.gif)

And this:
Clap providers:
[Clap providers](https://github.com/liuchengxu/vim-clap#providers)

And this:
![Clap providers](https://raw.githubusercontent.com/ray-x/ray-x.github.io/master/img/clap-providers.jpg)

Yes, it also provide a preview window......
Clap preview:
![Clap preview window](https://raw.githubusercontent.com/ray-x/ray-x.github.io/master/img/clap-preview.jpg)


You can replace you fzf commands with vim-clap, e.g. my vimrc:
```vim
noremap <leader><s-F> :Clap grep2 ++query=<cword><CR>
cmap <leader><S-F>h :Clap command_history<CR>
noremap <leader>ch :Clap command_history<CR>
noremap <leader>cf :Clap history<CR>


function! s:history(arg)
  let l:query=''
  let l:subcommand=''
  echo a:arg
  if len(a:arg) > 0
  	let l:query=' ++query='+a:arg[1]
  endif

  if a:arg[0] == ':'
    let l:subcommand = 'command_history'
    let l:query=trim(a:arg[1:])
  elseif a:arg[0] == '/'
    let l:subcommand = 'search_history'
    let l:query=trim(a:arg[1:])
  else
    let l:subcommand = 'history'
    let l:query=trim(a:arg)
  endif

  if len(l:query) > 1
    let l:query=' ++query=' . l:query
  endif
  exec 'Clap '. l:subcommand . l:query

endfunction

" noremap <c-F>:Clap grep2 ++query=@visual<CR>
noremap <s-T> :Clap tags<CR>
nmap <S-F2> :Clap filer<CR>

command! -bang -nargs=* History call s:history(<q-args>)
command! Files :Clap files
command! Buffers :Clap buffers
command! Tags :Clap proj_tags
command! Buffers :Clap buffers
command! Commits :Clap commits
command! Gdiff :Clap git_diff_files
command! Jumps :Clap jumps
command! Yanks :Clap yanks
command! Windows :Clap windows
command! Ag :Clap grep ++query<cword>
command! Ag2 :Clap grep2 ++query<cword>

```

So in command mode, when you type `History` `History!` `History:` it will provides similar interface as fzf
