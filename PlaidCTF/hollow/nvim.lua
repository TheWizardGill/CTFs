-- build container as `docker build --platform linux/arm64/v8 -t hollow-lsp .`
vim.lsp.start({
	name = "hollow-lsp",
	cmd = { "docker", "run", "-i", "--platform", "linux/arm64/v8", "hollow-lsp" },
	-- cmd = { "./bin/hollow-lsp" }
	root_dir = vim.fn.getcwd(),
})
vim.keymap.set('n', 'K', vim.lsp.buf.hover, {})
