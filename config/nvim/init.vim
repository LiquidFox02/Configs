source $HOME/.config/nvim/vim-plug/plugins.vim
source $HOME/.config/nvim/colorschemes.vim
source $HOME/.config/nvim/themes/airline.vim
echom "HEYYY JUUUUUUDEEEE!"
"GENERAL SETTINGS
syntax enable
set encoding=UTF-8
set background=dark
set mouse=a
set colorcolumn=80 
set noerrorbells
set noswapfile
set tabstop=4 shiftwidth=4
"set listchars=tab:\|\ 
"set list
" Display different types of white spaces.
set list
"set listchars=tab:›\ ,trail:•,extends:#,nbsp:.
set listchars=tab:.\ ,trail:•,extends:#,nbsp:.
set number relativenumber
set nohlsearch incsearch
set autoread
set undofile
set hidden
set updatetime=50
set termguicolors
set nobackup
set shortmess+=c
set nowrap
set smartcase
set smartindent
set inccommand=nosplit
set noshowmode
set undodir=~/.config/nvim/undodir
set splitbelow                          " Horizontal splits will automatically be below
set splitright                          " Vertical splits will automatically be to the right
set clipboard+=unnamedplus              " integrations with syatem clipboard
"highlight Normal guibg=none
"highlight NonText guibg=none
if executable('rg')
	let g:rg_derive_root='true'
endif
command! -bang -nargs=* Rg call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case ".shellescape(<q-args>), 1, {'options': '--delimiter : --nth 4..'}, <bang>0)
let g:netrw_browse_split=2
let g:netrw_winsize = 25
let g:netrw_banner = 0
let g:netrw_buffersettings = 'noma nomod nu nobl nowrap ro'
let g:python3_host_prog = '/home/ranchhor/anaconda3/envs/pynvim/bin/python'
"KEYBINDINGS OF SORTS
"Leader key
let mapleader = " "
let g:ctrlp_use_caching = 0
noremap <leader>h :wincmd h<CR>
noremap <leader>j :wincmd j<CR>
noremap <leader>k :wincmd k<CR>
noremap <leader>l :wincmd l<CR>
noremap <leader>u :UndotreeShow<CR>
noremap <leader>pv :wincmd v<bar> :Ex <bar> :vertical resize 30<CR>
noremap <leader>ps :Rg<SPACE>
noremap <silent> <leader>+ :vertical resize +5<CR>
noremap <silent> <leader>- :vertical resize -5<CR>
noremap <silent> <c-f> : Files<CR>
noremap <silent> <leader>F :Rg<CR>
inoremap <C-s> <esc>:w<cr>                 " save files
nnoremap <C-s> :w<cr>
inoremap <C-d> <esc>:wq!<cr>               " save and exit
nnoremap <C-d> :wq!<cr>
inoremap <C-q> <esc>:q!<cr>               " quit discarding changes
nnoremap <C-q> :q!<cr>
nmap <leader>f :NERDTreeToggle<cr>
nnoremap <leader>b :bprev<cr>
nnoremap <leader>n :bnext<cr>
"Compiling inside nvim using <F6>
map <F6> :call CompileRun()<CR>
func! CompileRun()
exec "w"
if &filetype == 'c'
exec "!gcc % -o %<"
exec "!time ./%<"
elseif &filetype == 'cpp'
exec "!g++ % -o %<"
exec "!time ./%<"
elseif &filetype == 'java'
"exec "javac %"
exec "!time java %"
"exec "!time java -cp %:p:h %:t:r"
elseif &filetype == 'sh'
exec "!time bash %"
elseif &filetype == 'python'
exec "!time python3 %"
elseif &filetype == 'html'
exec "!firefox % &"
elseif &filetype == 'go'
exec "!go build %<"
exec "!time go run %"
elseif &filetype == 'mkd'
exec "!~/.vim/markdown.pl % > %.html &"
exec "!firefox %.html &"
endif
endfunc
"for some reason the airline_theme couldn't be sourced from another
let g:Powerline_symbols = 'fancy'
set encoding=utf-8
set t_Co=256
set fillchars+=stl:\ ,stlnc:\
let g:Powerline_mode_V="V·LINE"
let g:Powerline_mode_cv="V·BLOCK"
let g:Powerline_mode_S="S·LINE"
let g:Powerline_mode_cs="S·BLOCK"
let g:airline_theme='gruvbox'
"treesitter settings for better syntax highlighting
lua << EOF
require'nvim-treesitter.configs'.setup
{
  ensure_installed = "maintained", -- one of "all", "maintained" (parsers with maintainers), or a list of languages
  highlight = {
    enable = true,              -- false will disable the whole extension
    disable = {"rust" },  -- list of language that will be disabled
  },
}
EOF
