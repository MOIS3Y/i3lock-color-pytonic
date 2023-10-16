#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
█░░ █▀█ █▀▀ █▄▀  █▀ █▀▀ █▀█ █▀▀ █▀▀ █▄░█ ▀
█▄▄ █▄█ █▄▄ █░█  ▄█ █▄▄ █▀▄ ██▄ ██▄ █░▀█ ▄
https://github.com/Raymo111/i3lock-color
-- -- -- -- -- -- -- -- -- -- -- -- -- --
Usage: i3lock.py [-h] [-s SCHEME] [-а FONT] [-t] [-v]

Wrapper over i3lock-color with a choice of color schemes

options:
  -h, --help                  show this help message and exit
  -s SCHEME, --scheme SCHEME  set color scheme name
  -f FONT,   --font FONT      set font style
  -t,        --themes         show available themes
  -v,        --version        show version


Color schemes are already set.
For portability, I copied all 35 color schemes here
previously collected in the library.
base16-colorlib (pip install base16-colorlib).
The library contains a collection of popular color schemes as well
as the Color class which can help change the color tints (HSL)
of individual elements.

Dependencies:
-- -- -- --
-i3lock-color
"""


# █▀▄▀█ █▀▀ ▀█▀ ▄▀█ ▀
# █░▀░█ ██▄ ░█░ █▀█ ▄
# -------------------
__author__ = "MOIS3Y"
__credits__ = ["Stepan Zhukovsky"]
__license__ = "GPL v3.0"
__version__ = "0.1.0"
__maintainer__ = "Stepan Zhukovsky"
__email__ = "stepan@zhukovsky.me"
__status__ = "Production"


import argparse
import subprocess


color_schemes = {
    'aquarium': {
        'scheme': 'aquarium',
        'author': 'https://github.com/FrenzyExists/aquarium-vim',
        'base00': '#20202a',
        'base01': '#2c2e3e',
        'base02': '#3d4059',
        'base03': '#313449',
        'base04': '#63718b',
        'base05': '#bac0cb',
        'base06': '#c5cbd6',
        'base07': '#ced4df',
        'base08': '#ebb9b9',
        'base09': '#e8cca7',
        'base0A': '#e6dfb8',
        'base0B': '#b1dba4',
        'base0C': '#b8dceb',
        'base0D': '#a3b8ef',
        'base0E': '#f6bbe7',
        'base0F': '#eac1c1',
    },
    'ashes': {
        'scheme': 'ashes',
        'author': 'https://github.com/chriskempson/base16-vim',
        'base00': '#1c2023',
        'base01': '#272b2e',
        'base02': '#303437',
        'base03': '#44484b',
        'base04': '#adb3ba',
        'base05': '#c7ccd1',
        'base06': '#dfe2e5',
        'base07': '#f3f4f5',
        'base08': '#c7ae95',
        'base09': '#c7c795',
        'base0A': '#aec795',
        'base0B': '#95c7ae',
        'base0C': '#95aec7',
        'base0D': '#ae95c7',
        'base0E': '#c795ae',
        'base0F': '#c79595',
    },
    'ayu_dark': {
        'scheme': 'ayu_dark',
        'author': 'https://github.com/ayu-theme/ayu-vim',
        'base00': '#0b0e14',
        'base01': '#1c1f25',
        'base02': '#24272d',
        'base03': '#2b2e34',
        'base04': '#33363c',
        'base05': '#c9c7be',
        'base06': '#e6e1cf',
        'base07': '#d9d7ce',
        'base08': '#c9c7be',
        'base09': '#ffee99',
        'base0A': '#56c3f9',
        'base0B': '#aad84c',
        'base0C': '#ffb454',
        'base0D': '#f07174',
        'base0E': '#ffb454',
        'base0F': '#cba6f7',
    },
    'ayu_light': {
        'scheme': 'ayu_light',
        'author': 'https://github.com/ayu-theme/ayu-vim',
        'base00': '#fafafa',
        'base01': '#f0f0f0',
        'base02': '#eeeeee',
        'base03': '#dfdfdf',
        'base04': '#d2d2d2',
        'base05': '#5c6166',
        'base06': '#52575c',
        'base07': '#484d52',
        'base08': '#f07171',
        'base09': '#a37acc',
        'base0A': '#399ee6',
        'base0B': '#86b300',
        'base0C': '#4cbf99',
        'base0D': '#55b4d4',
        'base0E': '#fa8d3e',
        'base0F': '#f2ae49',
    },
    'bearded_arc': {
        'scheme': 'bearded_arc',
        'author': 'https://github.com/BeardedBear/bearded-theme',
        'base00': '#1c2433',
        'base01': '#262e3d',
        'base02': '#303847',
        'base03': '#444c5b',
        'base04': '#a1adb7',
        'base05': '#c3cfd9',
        'base06': '#abb7c1',
        'base07': '#08bdba',
        'base08': '#ff738a',
        'base09': '#ff955c',
        'base0A': '#eacd61',
        'base0B': '#3cec85',
        'base0C': '#77aed7',
        'base0D': '#69c3ff',
        'base0E': '#22ecdb',
        'base0F': '#ff738a',
    },
    'blossom_light': {
        'scheme': 'blossom_light',
        'author': 'https://github.com/blossom-theme',
        'base00': '#e6dfdc',
        'base01': '#ded7d4',
        'base02': '#d7d0cd',
        'base03': '#d1cac7',
        'base04': '#cac3c0',
        'base05': '#746862',
        'base06': '#5e524c',
        'base07': '#695d57',
        'base08': '#8779a8',
        'base09': '#a87678',
        'base0A': '#738199',
        'base0B': '#6c805c',
        'base0C': '#5e908e',
        'base0D': '#b3816a',
        'base0E': '#7e8e8e',
        'base0F': '#976153',
    },
    'catppuccin_latte': {
        'scheme': 'catppuccin_latte',
        'author': 'https://github.com/catppuccin/catppuccin',
        'base00': '#eff1f5',  # base
        'base01': '#e6e9ef',  # mantle
        'base02': '#ccd0da',  # surface0
        'base03': '#bcc0cc',  # surface1
        'base04': '#acb0be',  # surface2
        'base05': '#4c4f69',  # text
        'base06': '#dc8a78',  # rosewater
        'base07': '#7287fd',  # lavender
        'base08': '#d20f39',  # red
        'base09': '#fe640b',  # peach
        'base0A': '#df8e1d',  # yellow
        'base0B': '#40a02b',  # green
        'base0C': '#179299',  # teal
        'base0D': '#1e66f5',  # blue
        'base0E': '#8839ef',  # mauve
        'base0F': '#dd7878',  # flamingo
    },
    'catppuccin_frappe': {
        'scheme': 'catppuccin_frappe',
        'author': 'https://github.com/catppuccin/catppuccin',
        'base00': '#303446',  # base
        'base01': '#292c3c',  # mantle
        'base02': '#414559',  # surface0
        'base03': '#51576d',  # surface1
        'base04': '#626880',  # surface2
        'base05': '#c6d0f5',  # text
        'base06': '#f2d5cf',  # rosewater
        'base07': '#babbf1',  # lavender
        'base08': '#e78284',  # red
        'base09': '#ef9f76',  # peach
        'base0A': '#e5c890',  # yellow
        'base0B': '#a6d189',  # green
        'base0C': '#81c8be',  # teal
        'base0D': '#8caaee',  # blue
        'base0E': '#ca9ee6',  # mauve
        'base0F': '#eebebe',  # flamingo
    },
    'catppuccin_macchiato': {
        'scheme': 'catppuccin_macchiato',
        'author': 'https://github.com/catppuccin/catppuccin',
        'base00': '#24273a',  # base
        'base01': '#1e2030',  # mantle
        'base02': '#363a4f',  # surface0
        'base03': '#494d64',  # surface1
        'base04': '#5b6078',  # surface2
        'base05': '#cad3f5',  # text
        'base06': '#f4dbd6',  # rosewater
        'base07': '#b7bdf8',  # lavender
        'base08': '#ed8796',  # red
        'base09': '#f5a97f',  # peach
        'base0A': '#eed49f',  # yellow
        'base0B': '#a6da95',  # green
        'base0C': '#8bd5ca',  # teal
        'base0D': '#8aadf4',  # blue
        'base0E': '#c6a0f6',  # mauve
        'base0F': '#f0c6c6',  # flamingo
    },
    'catppuccin_mocha': {
        'scheme': 'catppuccin_mocha',
        'author': 'https://github.com/catppuccin/catppuccin',
        'base00': '#11111b',  # crust
        'base01': '#1e1e2e',  # base
        'base02': '#313244',  # surface0
        'base03': '#45475a',  # surface1
        'base04': '#585b70',  # surface2
        'base05': '#cdd6f4',  # text
        'base06': '#f5e0dc',  # rosewater
        'base07': '#b4befe',  # lavender
        'base08': '#f38ba8',  # red
        'base09': '#fab387',  # peach
        'base0A': '#f9e2af',  # yellow
        'base0B': '#a6e3a1',  # green
        'base0C': '#94e2d5',  # teal
        'base0D': '#89b4fa',  # blue
        'base0E': '#cba6f7',  # mauve
        'base0F': '#f2cdcd',  # flamingo
    },
    'dracula': {
        'scheme': 'dracula',
        'author': 'https://github.com/dracula',
        'base00': '#282936',
        'base01': '#3a3c4e',
        'base02': '#4d4f68',
        'base03': '#626483',
        'base04': '#62d6e8',
        'base05': '#e9e9f4',
        'base06': '#f1f2f8',
        'base07': '#f7f7fb',
        'base08': '#ea51b2',
        'base09': '#b45bcf',
        'base0A': '#00f769',
        'base0B': '#ebff87',
        'base0C': '#a1efe4',
        'base0D': '#62d6e8',
        'base0E': '#b45bcf',
        'base0F': '#00f769',
    },
    'decay': {
        'scheme': 'decay',
        'author': 'https://github.com/decaycs',
        'base00': '#171b20',
        'base01': '#21262e',
        'base02': '#242931',
        'base03': '#485263',
        'base04': '#485263',
        'base05': '#b6beca',
        'base06': '#dee1e6',
        'base07': '#dee1e6',
        'base08': '#70a5eb',
        'base09': '#e9a180',
        'base0A': '#f1cf8a',
        'base0B': '#78dba9',
        'base0C': '#e26c7c',
        'base0D': '#86aaec',
        'base0E': '#c68aee',
        'base0F': '#9cd1ff',
    },
    'everblush': {
        'scheme': 'everblush',
        'author': 'https://github.com/Everblush',
        'base00': '#141b1e',
        'base01': '#1e2528',
        'base02': '#282f32',
        'base03': '#2d3437',
        'base04': '#3c4346',
        'base05': '#dadada',
        'base06': '#e4e4e4',
        'base07': '#dadada',
        'base08': '#e57474',
        'base09': '#fcb163',
        'base0A': '#e5c76b',
        'base0B': '#8ccf7e',
        'base0C': '#6cbfbf',
        'base0D': '#67b0e8',
        'base0E': '#c47fd5',
        'base0F': '#ef7d7d',
    },
    'everforest_dark': {
        'scheme': 'everforest_dark',
        'author': 'https://github.com/sainnhe/everforest',
        'base00': '#2b3339',
        'base01': '#323c41',
        'base02': '#3a4248',
        'base03': '#424a50',
        'base04': '#4a5258',
        'base05': '#d3c6aa',
        'base06': '#ddd0b4',
        'base07': '#e7dabe',
        'base08': '#7fbbb3',
        'base09': '#d699b6',
        'base0A': '#83c092',
        'base0B': '#dbbc7f',
        'base0C': '#e69875',
        'base0D': '#a7c080',
        'base0E': '#e67e80',
        'base0F': '#d699b6',
    },
    'everforest_light': {
        'scheme': 'everforest_light',
        'author': 'https://github.com/sainnhe/everforest',
        'base00': '#fff9e8',
        'base01': '#f6f0df',
        'base02': '#ede7d6',
        'base03': '#e5dfce',
        'base04': '#ddd7c6',
        'base05': '#495157',
        'base06': '#3b4349',
        'base07': '#272f35',
        'base08': '#5f9b93',
        'base09': '#b67996',
        'base0A': '#8da101',
        'base0B': '#d59600',
        'base0C': '#ef615e',
        'base0D': '#87a060',
        'base0E': '#c85552',
        'base0F': '#c85552',
    },
    'falcon': {
        'scheme': 'falcon',
        'author': 'https://github.com/fenetikm/falcon',
        'base00': '#020222',
        'base01': '#0b0b2b',
        'base02': '#161636',
        'base03': '#202040',
        'base04': '#e4e4eb',
        'base05': '#eeeef5',
        'base06': '#f3f3fa',
        'base07': '#f8f8ff',
        'base08': '#bfdaff',
        'base09': '#b4b4b9',
        'base0A': '#ffc552',
        'base0B': '#c8d0e3',
        'base0C': '#b4b4b9',
        'base0D': '#ffc552',
        'base0E': '#8bccbf',
        'base0F': '#dfdfe5',
    },
    'gruvbox_dark': {
        'scheme': 'gruvbox_dark',
        'author': 'https://github.com/morhetz/gruvbox',
        'base00': '#282828',
        'base01': '#3c3836',
        'base02': '#423e3c',
        'base03': '#484442',
        'base04': '#bdae93',
        'base05': '#d5c4a1',
        'base06': '#ebdbb2',
        'base07': '#fbf1c7',
        'base08': '#fb4934',
        'base09': '#fe8019',
        'base0A': '#fabd2f',
        'base0B': '#b8bb26',
        'base0C': '#8ec07c',
        'base0D': '#83a598',
        'base0E': '#d3869b',
        'base0F': '#d65d0e',
    },
    'gruvbox_light': {
        'scheme': 'gruvbox_light',
        'author': 'https://github.com/morhetz/gruvbox',
        'base00': '#f2e5bc',
        'base01': '#e3d6ad',
        'base02': '#e5d8af',
        'base03': '#d8cba2',
        'base04': '#cabd94',
        'base05': '#504945',
        'base06': '#3c3836',
        'base07': '#282828',
        'base08': '#9d0006',
        'base09': '#af3a03',
        'base0A': '#b57614',
        'base0B': '#79740e',
        'base0C': '#427b58',
        'base0D': '#076678',
        'base0E': '#8f3f71',
        'base0F': '#d65d0e',
    },
    'kanagawa': {
        'scheme': 'kanagawa',
        'author': 'https://github.com/rebelot/kanagawa.nvim',
        'base00': '#1f1f28',
        'base01': '#2a2a37',
        'base02': '#223249',
        'base03': '#363646',
        'base04': '#4c4c55',
        'base05': '#c8c3a6',
        'base06': '#d2cdb0',
        'base07': '#dcd7ba',
        'base08': '#d8616b',
        'base09': '#ffa066',
        'base0A': '#dca561',
        'base0B': '#98bb6c',
        'base0C': '#7fb4ca',
        'base0D': '#7e9cd8',
        'base0E': '#9c86bf',
        'base0F': '#d8616b',
    },
    'melange': {
        'scheme': 'melange',
        'author': 'https://github.com/savq/melange',
        'base00': '#2a2520',
        'base01': '#39342f',
        'base02': '#433e39',
        'base03': '#4d4843',
        'base04': '#57524d',
        'base05': '#ece1d7',
        'base06': '#e3d8ce',
        'base07': '#d8cdc3',
        'base08': '#ece1d7',
        'base09': '#86a3a3',
        'base0A': '#99d59d',
        'base0B': '#9aacce',
        'base0C': '#ebc06d',
        'base0D': '#ebc06d',
        'base0E': '#e49b5d',
        'base0F': '#8e733f',
    },
    'monokai': {
        'scheme': 'monokai',
        'author': 'https://monokai.pro',
        'base00': '#272822',
        'base01': '#383830',
        'base02': '#49483e',
        'base03': '#75715e',
        'base04': '#a59f85',
        'base05': '#f8f8f2',
        'base06': '#f5f4f1',
        'base07': '#f9f8f5',
        'base08': '#fd971f',
        'base09': '#ae81ff',
        'base0A': '#f4bf75',
        'base0B': '#a6e22e',
        'base0C': '#a1efe4',
        'base0D': '#66d9ef',
        'base0E': '#f92672',
        'base0F': '#cc6633',
    },
    'monochrome': {
        'scheme': 'monochrome',
        'author': 'https://github.com/kdheepak/monochrome.nvim',
        'base00': '#101010',
        'base01': '#1f1f1f',
        'base02': '#2e2e2e',
        'base03': '#383838',
        'base04': '#424242',
        'base05': '#bfc5d0',
        'base06': '#c7cdd8',
        'base07': '#ced4df',
        'base08': '#eee8d5',
        'base09': '#b8b7b1',
        'base0A': '#859ba2',
        'base0B': '#7b9198',
        'base0C': '#dfdfda',
        'base0D': '#ced4df',
        'base0E': '#dad4c3',
        'base0F': '#ced4df',
    },
    'mountain': {
        'scheme': 'mountain',
        'author': 'https://github.com/mountain-theme/Mountain',
        'base00': '#0f0f0f',
        'base01': '#151515',
        'base02': '#191919',
        'base03': '#222222',
        'base04': '#535353',
        'base05': '#d8d8d8',
        'base06': '#e6e6e6',
        'base07': '#f0f0f0',
        'base08': '#b18f91',
        'base09': '#d8bb92',
        'base0A': '#b1ae8f',
        'base0B': '#8aac8b',
        'base0C': '#91b2b3',
        'base0D': '#a5a0c2',
        'base0E': '#ac8aac',
        'base0F': '#b39193',
    },
    'nord': {
        'scheme': 'nord',
        'author': 'https://www.nordtheme.com',
        'base00': '#2e3440',
        'base01': '#3b4252',
        'base02': '#434c5e',
        'base03': '#4c566a',
        'base04': '#d8dee9',
        'base05': '#e5e9f0',
        'base06': '#eceff4',
        'base07': '#8fbcbb',
        'base08': '#88c0d0',
        'base09': '#81a1c1',
        'base0A': '#5e81ac',
        'base0B': '#bf616a',
        'base0C': '#d08770',
        'base0D': '#ebcb8b',
        'base0E': '#a3be8c',
        'base0F': '#b48ead',
    },
    'onedark': {
        'scheme': 'onedark',
        'author': 'https://github.com/one-dark',
        'base00': '#1e222a',
        'base01': '#353b45',
        'base02': '#3e4451',
        'base03': '#545862',
        'base04': '#565c64',
        'base05': '#abb2bf',
        'base06': '#b6bdca',
        'base07': '#c8ccd4',
        'base08': '#e06c75',
        'base09': '#d19a66',
        'base0A': '#e5c07b',
        'base0B': '#98c379',
        'base0C': '#56b6c2',
        'base0D': '#61afef',
        'base0E': '#c678dd',
        'base0F': '#be5046',
    },
    'onelight': {
        'scheme': 'onelight',
        'author': 'https://github.com/one-dark',
        'base00': '#fafafa',
        'base01': '#f4f4f4',
        'base02': '#e5e5e6',
        'base03': '#dfdfe0',
        'base04': '#d7d7d8',
        'base05': '#383a42',
        'base06': '#202227',
        'base07': '#090a0b',
        'base08': '#d84a3d',
        'base09': '#a626a4',
        'base0A': '#c18401',
        'base0B': '#50a14f',
        'base0C': '#0070a8',
        'base0D': '#4078f2',
        'base0E': '#a626a4',
        'base0F': '#986801',
    },
    'rosepine': {
        'scheme': 'rosepine',
        'author': 'https://github.com/edunfelt/base16-rose-pine-scheme',
        'base00': '#191724',
        'base01': '#1f1d2e',
        'base02': '#26233a',
        'base03': '#6e6a86',
        'base04': '#908caa',
        'base05': '#e0def4',
        'base06': '#e0def4',
        'base07': '#524f67',
        'base08': '#eb6f92',
        'base09': '#f6c177',
        'base0A': '#ebbcba',
        'base0B': '#31748f',
        'base0C': '#9ccfd8',
        'base0D': '#c4a7e7',
        'base0E': '#f6c177',
        'base0F': '#524f67',
    },
    'rosepine_moon': {
        'scheme': 'rosepine_moon',
        'author': 'https://github.com/edunfelt/base16-rose-pine-scheme',
        'base00': '#232136',
        'base01': '#2a273f',
        'base02': '#393552',
        'base03': '#6e6a86',
        'base04': '#908caa',
        'base05': '#e0def4',
        'base06': '#56526e',
        'base07': '#ecebf0',
        'base08': '#eb6f92',
        'base09': '#f6c177',
        'base0A': '#ea9a97',
        'base0B': '#3e8fb0',
        'base0C': '#9ccfd8',
        'base0D': '#c4a7e7',
        'base0E': '#f6c177',
        'base0F': '#56526e',
    },
    'rosepine_dawn': {
        'scheme': 'rosepine_dawn',
        'author': 'https://github.com/edunfelt/base16-rose-pine-scheme',
        'base00': '#faf4ed',
        'base01': '#fffaf3',
        'base02': '#f2e9de',
        'base03': '#9893a5',
        'base04': '#797593',
        'base05': '#575279',
        'base06': '#575279',
        'base07': '#cecacd',
        'base08': '#b4637a',
        'base09': '#ea9d34',
        'base0A': '#d7827e',
        'base0B': '#286983',
        'base0C': '#56949f',
        'base0D': '#907aa9',
        'base0E': '#ea9d34',
        'base0F': '#cecacd',
    },
    'rxyhn': {
        'scheme': 'rxyhn',
        'author': 'https://github.com/rxyhn/yoru',
        'base00': '#061115',
        'base01': '#0c171b',
        'base02': '#101b1f',
        'base03': '#192428',
        'base04': '#212c30',
        'base05': '#d9d7d6',
        'base06': '#e3e1e0',
        'base07': '#edebea',
        'base08': '#f26e74',
        'base09': '#ecd28b',
        'base0A': '#e9967e',
        'base0B': '#82c29c',
        'base0C': '#6791c9',
        'base0D': '#79aaeb',
        'base0E': '#c488ec',
        'base0F': '#f16269',
    },
    'solarized': {
        'scheme': 'solarized',
        'author': 'https://github.com/altercation/solarized',
        'base00': '#002b36',
        'base01': '#06313c',
        'base02': '#0a3540',
        'base03': '#133e49',
        'base04': '#1b4651',
        'base05': '#93a1a1',
        'base06': '#eee8d5',
        'base07': '#fdf6e3',
        'base08': '#dc322f',
        'base09': '#cb4b16',
        'base0A': '#b58900',
        'base0B': '#859900',
        'base0C': '#2aa198',
        'base0D': '#268bd2',
        'base0E': '#6c71c4',
        'base0F': '#d33682',
    },
    'sweetpastel': {
        'scheme': 'sweetpastel',
        'author': 'https://github.com/SweetPastel',
        'base00': '#1b1f23',
        'base01': '#25292d',
        'base02': '#2f3337',
        'base03': '#393d41',
        'base04': '#43474b',
        'base05': '#fde5e6',
        'base06': '#dee2e6',
        'base07': '#f8f9fa',
        'base08': '#e5a3a1',
        'base09': '#f1c192',
        'base0A': '#ece3b1',
        'base0B': '#b4e3ad',
        'base0C': '#f8b3cc',
        'base0D': '#a3cbe7',
        'base0E': '#ceace8',
        'base0F': '#e5a3a1',
    },
    'tokyodark': {
        'scheme': 'tokyodark',
        'author': 'https://github.com/tiagovla/tokyodark.nvim',
        'base00': '#11121d',
        'base01': '#1b1c27',
        'base02': '#21222d',
        'base03': '#282934',
        'base04': '#30313c',
        'base05': '#abb2bf',
        'base06': '#b2b9c6',
        'base07': '#a0a8cd',
        'base08': '#ee6d85',
        'base09': '#7199ee',
        'base0A': '#7199ee',
        'base0B': '#dfae67',
        'base0C': '#a485dd',
        'base0D': '#95c561',
        'base0E': '#a485dd',
        'base0F': '#f3627a',
    },
    'tokyonight': {
        'scheme': 'tokyonight',
        'author': 'https://github.com/tiagovla/tokyonight.nvim',
        'base00': '#1a1b26',
        'base01': '#16161e',
        'base02': '#2f3549',
        'base03': '#444b6a',
        'base04': '#787c99',
        'base05': '#a9b1d6',
        'base06': '#cbccd1',
        'base07': '#d5d6db',
        'base08': '#73daca',
        'base09': '#ff9e64',
        'base0A': '#0db9d7',
        'base0B': '#9ece6a',
        'base0C': '#b4f9f8',
        'base0D': '#2ac3de',
        'base0E': '#bb9af7',
        'base0F': '#f7768e',
    },
    'yoru': {
        'scheme': 'yoru',
        'author': 'https://github.com/rxyhn/yoru',
        'base00': '#0c0e0f',
        'base01': '#121415',
        'base02': '#161819',
        'base03': '#1f2122',
        'base04': '#27292a',
        'base05': '#edeff0',
        'base06': '#e4e6e7',
        'base07': '#f2f4f5',
        'base08': '#f26e74',
        'base09': '#ecd28b',
        'base0A': '#e79881',
        'base0B': '#82c29c',
        'base0C': '#6791c9',
        'base0D': '#709ad2',
        'base0E': '#c58cec',
        'base0F': '#e8646a',
    }
}


# -- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- --
def i3lock_run(colors, font):
    try:
        subprocess.run([
            # bin:
            'i3lock',
            # params:
            '--screen=1',
            '--blur=2',
            '--clock',
            '--indicator',
            '--line-uses-ring',
            '--radius=110',
            '--ring-width=9',
            '--keylayout=1',
            # colors:
            f'--insidever-color={colors["base02"]}',    # surface
            f'--insidewrong-color={colors["base02"]}',  # surface
            f'--inside-color={colors["base00"]}',       # crust
            f'--ringver-color={colors["base0B"]}',      # green
            f'--ringwrong-color={colors["base08"]}',    # red
            f'--ringver-color={colors["base0B"]}',      # green
            f'--ringwrong-color={colors["base08"]}',    # red
            f'--ring-color={colors["base02"]}',         # surface
            f'--keyhl-color={colors["base0D"]}',        # blue
            f'--bshl-color={colors["base0A"]}',         # yellow
            f'--verif-color={colors["base0B"]}',        # green
            f'--wrong-color={colors["base08"]}',        # red
            f'--layout-color={colors["base0D"]}',       # blue
            f'--separator-color={colors["base05"]}',    # text
            f'--date-color={colors["base05"]}',         # text
            f'--time-color={colors["base05"]}',         # text
            f'--modif-color={colors["base05"]}',        # text
            # font:
            f'--time-font={font}',
            f'--date-font={font}',
            f'--layout-font={font}',
            f'--verif-font={font}',
            f'--wrong-font={font}',
            # text:
            '--time-str=%T',  # %I:%M %p (am/pm)
            '--date-str=%a, %e %b %Y',
            '--verif-text=Verifying...',
            '--wrong-text=Auth Failed',
            '--noinput=No Input',
            '--lock-text=Locking...',
            '--lockfailed=Lock Failed',
            # pass keys:
            '--pass-media-keys',
            '--pass-screen-keys',
            '--pass-volume-keys',
        ])
    except FileNotFoundError as error:
        print(f"i3lock not found.\n{error}")


def show_themes(**color_schemes):
    for scheme in [scheme for scheme in color_schemes]:
        print(scheme)


# entrypoint:
def main():
    parser = argparse.ArgumentParser(
        description='Wrapper over i3lock-color with a choice of color schemes'
    )
    parser.add_argument(
        '-s',
        '--scheme',
        type=str,
        help='set color scheme name'
    )
    parser.add_argument(
        '-f',
        '--font',
        default='Sans',
        type=str,
        help='set font style'
    )
    parser.add_argument(
        '-t',
        '--themes',
        action='store_true',
        help='show available themes'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help='show version'
    )
    args = parser.parse_args()

    # Show version:
    if args.version:
        print(__version__)
    # Show available color schemes:
    elif args.themes:
        show_themes(**color_schemes)
    # Run lockscreen:
    elif args.scheme:
        if args.scheme in color_schemes:
            i3lock_run(colors=color_schemes[args.scheme], font=args.font)
        else:
            show_themes(**color_schemes)
    else:
        i3lock_run(
            colors=color_schemes['catppuccin_mocha'],
            font='Sans'
        )


if __name__ == "__main__":
    main()
