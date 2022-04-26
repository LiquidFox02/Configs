" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')
	Plug 'sainnhe/everforest'
	Plug 'vimwiki/vimwiki'
	Plug 'junegunn/goyo.vim'
	Plug 'nvim-lua/popup.nvim'
    Plug 'nvim-lua/plenary.nvim'
    Plug 'nvim-telescope/telescope.nvim'
	Plug 'nvim-telescope/telescope-media-files.nvim'
	
    "Better starting screen for vim
	Plug 'mhinz/vim-startify'
	" Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " File Explorer
    Plug 'scrooloose/NERDTree'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    "Code Completion
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    "Airline theme
    Plug 'vim-airline/vim-airline'
    "Grubox color scheme
    Plug 'gruvbox-community/gruvbog'
    "File fzf
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'
	Plug 'yuki-ycino/fzf-preview.vim', { 'branch': 'release', 'do': ':UpdateRemotePlugins' }
    "Debugger
    Plug 'puremourning/vimspector'
    "Snippets
    Plug 'honza/vim-snippets'
    "Undo-Tree
    Plug 'mbbill/undotree'  
	"Terminal splitter
	Plug 'vimlab/split-term.vim'
	" Better Comments
    Plug 'tpope/vim-commentary'
    " Change dates fast
    Plug 'tpope/vim-speeddating'
    " Convert binary, hex, etc..
    Plug 'glts/vim-radical'
    " Repeat stuff
    Plug 'tpope/vim-repeat'
    " Text Navigation
    Plug 'unblevable/quick-scope'
    " " async tasks
    Plug 'skywind3000/asynctasks.vim'
    Plug 'skywind3000/asyncrun.vim'
    " Swap windows
    Plug 'wesQ3/vim-windowswap'
	"Rip Grep
	Plug 'jremmen/vim-ripgrep'
	"Cpp rtags
	Plug 'lyuts/vim-rtags'
	"better java syntax
	Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}  " We recommend updating the parsers on update
	"semantic highlighting for clangd
	"Plug 'jackguo380/vim-lsp-cxx-highlight'
	Plug 'rafi/awesome-vim-colorschemes'
	Plug 'ryanoasis/vim-devicons'
	call plug#end()

