---
title: Z shell
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/06/Z-shell/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7f4ce4deefa9a3a2'
translated: false
---

> 原文：[Z shell](https://belkadan.com/blog/2009/06/Z-shell/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [“Several New Features”](https://belkadan.com/blog/2009/05/Several-New-Features/)

[Garbage Collectors and Stack Drawers](https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/) »

« [HTTPS and Name-based Virtual Hosting](https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/?tag=unix)

[Priorities](https://belkadan.com/blog/2011/07/Priorities/?tag=unix) »

[\> go east](https://belkadan.com/blog/2019/08/go-east/?tag=shell) »

## [Z shell](#)

Failing to keep up with my (bi)weekly postings, I return nonetheless to post something of interest to fellow developers. This post is on my latest Unix-shell-of-choice, the Z shell (zsh).

For a long time I was a bash user, actually since a little after the switch from tcsh to bash in Panther. Bash (the “Bourne-again shell”) is useful and dependable and doesn’t pretend to be something it’s not, something I felt tcsh (and the C shell family in general) was occasionally guilty of. But I got fed up with the context-insensitive completions and uncustomizable keyboard shortcuts, at about the same time. And bash just wasn’t that customizable/extensible.

Enter zsh. I’d read about it online before, and figured it would be close enough to bash for me to switch to it even without learning new features. But I could turn on whatever new features I wanted.

Rather than narrate my experiences setting up the various dotfiles, getting used to the small differences, and so on, I’ll just note that the default zsh support for completion of SVN commands was a little broken, and that there’s a replacement in the GVN repository ([instructions here](http://malsserver.blogspot.com/2009/02/zsh-tab-completion-fix-for-subversion.html) – drop the “Completion/Unix/” from the path, though). Besides that, here are the interesting parts of my .zshrc file.

```
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zhistory
setopt INC_APPEND_HISTORY
```

Zsh doesn’t save command history across sessions by default, so this is a pretty simple enabling of that. On the other hand, there’s an extraordinarily complex shortcut system for getting lines or even individual arguments out of the history. I am not yet familiar with this and stick to the good old `!`_`command`_ and `!!`

```
bindkey -e  # emacs key bindings
bindkey "\e\e[C" vi-forward-word
bindkey "\e\e[D" vi-backward-word
```

Key bindings! The emacs key bindings have written themselves into my fingers by now, so being able to use them in the shell is great. On the other hand, I haven’t yet found the right granularity for jumping words, but in the meantime I’m using vi’s definition. `\e\e[C` and `\e\e[D` are Option-Right and Option-Left, respectively.

```
setopt PROMPT_SUBST
PROMPT='[%~] %n%# '
autoload colors; colors
# what is this disgustingly complicated bit?
# if the last command failed, print it in red in parentheses
# before the close paren, print the status in black
# make sure to ESCAPE the last command's % and ) signs
RPROMPT='  %(?..%{$fg[red]%}(%15>…>`echo ${${$(fc -ln -1)//\%/%%}//)/%)}`%>>
 %{$fg[black]%}%?%{$fg[red]%}%)%{$fg[default]%})'
# if you use this, make sure to remove the newline
```

My prompt is pretty standard: path, username, and prompt character (% for normal user, # for privileged). But I wanted to make good use of the RPROMPT (right-hand-side prompt). Z shell is smart enough to hide the rprompt when you type out that far, so all I had to do was put it together. I’m not going to take it apart for you, but rest assured it took several tries to get right. (The problem is flipping between string data and shell commands – they look a lot like each other to me and to the expansion system.) The `colors` module is loaded to populate the $fg and $bg arrays with the right control codes for switching colors.

```
autoload -U compinit; compinit
setopt AUTO_CD
autoload zmv
```

The first line loads the amazing context-sensitive completion system, whose surface I have barely scratched. The second allows you to leave out CD and just put in a directory name to go there (useful for dragging folders in from the Finder). The last enables `zmv`, a smart file mover/renamer that supports batch operations and regular expressions. Very useful, though I still need to look up examples.

```
[[ $TERM = 'xterm-color' ]] && alias ssh='TERM=xterm ssh'
[[ $EMACS = t ]] && unsetopt zle
```

Some defensive options. Most ssh servers don’t like the “xterm-color” terminal type, so I use the plain “xterm” for my ssh client. And zsh doesn’t need to provide its fancy line editor when running inside emacs. (Actually, it apparently causes great problems if you leave this out.)

```
alias cp='cp -ir' # ask confirmation for overwrite, copy-recursive
alias mv='mv -i'  # ask confirmation for overwrite
alias rm='rm -id' # ask confirmation, remove directories too
alias ls='ls -Fh' # suffixes, human-readable sizes
alias l='ls -l'   # detail mode
alias la='ls -A'  # show hidden files, minus . and ..
alias ll='l -a'   # show all hidden files in detail mode

setopt IGNORE_EOF # don't log out on EOF
setopt NO_CLOBBER # don't overwrite files unless forced
```

And finally, some simple shell settings. Matters of preference.

That’s it for this week. Zsh really is “a better bash”. If you’ve been frustrated by bash’s shortcomings, give it a whirl. And remember that there are a ton more features than I’ve described here — read about them in the man pages, in [the zsh manual](http://zsh.dotsrc.org/Doc/Release/zsh_toc.html), or in many other example pages and blog posts online.

```
chsh -s /bin/zsh
```

This entry was posted on [June](https://belkadan.com/blog/2009/06) 21, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Unix](https://belkadan.com/blog/tags/unix), [Shell](https://belkadan.com/blog/tags/shell)
