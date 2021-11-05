# OS/FS

I run [Arch Linux](https://wiki.archlinux.org/title/Arch_Linux) on the
[Zen kernel](https://wiki.archlinux.org/title/Kernel) with the
[BTRFS](https://www.wikiwand.com/en/Btrfs#/Features) filesystem
utilizing incremental snapshots in
[Snapper](https://www.wikiwand.com/en/Btrfs#/Features) and
[grub-btrfs](https://github.com/Antynea/grub-btrfs) in case I need to
revert breaking changes from the grub menu on my machine. (haven't
needed to yet so :fingers_crossed:)

# dotfiles

All my configs managed with a [git --bare
repo](https://www.atlassian.com/git/tutorials/dotfiles), usually in
[lazygit](https://github.com/jesseduffield/lazygit) with the following
aliases in
[.config/fish/config.fish](https://github.com/JacobTravers/dotfiles/blob/main/.config/fish/config.fish#L148):

    # config = git for ~/dotfiles
    alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

    # lc = lazygit for ~/dotfiles
    alias lc='lazygit --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

## warehouse

[warehouse](https://github.com/JacobTravers/dotfiles/blob/main/.config/fish/functions/warehouse.fish)
is a fish script I made to keep a record of the installed packages on my
machine, it concatenates package names from various locations to
[.warehouse](https://github.com/JacobTravers/dotfiles/blob/main/.warehouse)
in my home directory. This also serves as a quick resource for anybody
curious about the packages on my system.

## kakrc

My kakoune config is almost entirely in
[kakrc](https://github.com/JacobTravers/dotfiles/blob/main/.config/kak/kakrc),
the only item outside of my kakrc that isn't simply managed by
[plug.kak](https://github.com/andreyorst/plug.kak) is
[kakoune.cr](https://github.com/alexherbo2/kakoune.cr)

### kak plugs:

-   [alacritty.kak](https://github.com/alexherbo2/alacritty.kak)
-   [auto-pairs.kak](https://github.com/alexherbo2/auto-pairs.kak)
-   [indent.kak](https://github.com/alexherbo2/indent.kak)
-   [show-whitespaces.kak](https://github.com/alexherbo2/show-whitespaces.kak)
-   [window.kak](https://github.com/alexherbo2/window.kak)
-   [plug.kak](https://github.com/andreyorst/plug.kak)
-   [kakoune-focus](https://github.com/caksoylar/kakoune-focus)
-   [kakoune-mysticaltutor](https://github.com/caksoylar/kakoune-mysticaltutor)
-   [kak-rainbower](https://github.com/crizan/kak-rainbower)
-   [kakoune-easymotion](https://github.com/danr/kakoune-easymotion)
-   [kakoune-buffers](https://github.com/delapouite/kakoune-buffers)
-   [kakpipe](https://github.com/eburghar/kakpipe)
-   [number-toggle.kak](https://github.com/evanrelf/number-toggle.kak)
-   [luar](https://github.com/gustavo-hms/luar)
-   [peneira](https://github.com/gustavo-hms/peneira)
-   [kakoune-surround](https://github.com/h-youhei/kakoune-surround)
-   [kakoune-grep-write](https://github.com/JacobTravers/kakoune-grep-write)
-   [kakoune-sudo-write](https://github.com/JacobTravers/kakoune-sudo-write)
-   [kak-lsp](https://github.com/kak-lsp/kak-lsp)
-   [ui.kak](https://github.com/kkga/ui.kak)
-   [kakboard](https://github.com/lePerdu/kakboard)
-   [kakoune-phantom-selection](https://github.com/occivink/kakoune-phantom-selection)
-   [kakoune-repl-buffer](https://gitlab.com/Screwtapello/kakoune-repl-buffer)
-   [kak-tree](https://github.com/ul/kak-tree)
-   [dynamic-matching.kak](https://github.com/useredsa/dynamic-matching.kak)
