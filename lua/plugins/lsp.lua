-- All things LSP in her-- All things LSP in here

-- Setup LSP with some nice default options
local setup_lsp = function(server_name, opts)
	opts = opts or {}
	local capabilities = vim.lsp.protocol.make_client_capabilities()
	capabilities = require("cmp_nvim_lsp").default_capabilities(capabilities)
	capabilities.textDocument.completion.completionItem.snippetSupport = true
	opts.capabilities = capabilities or {}
	opts.on_attach = function(client, bufnr)
		if client.supports_method("textDocument/hover") then
			vim.lsp.handlers["textDocument/hover"] = vim.lsp.with(vim.lsp.handlers.hover, { border = "rounded" })
		end
		if client.supports_method("textDocument/signatureHelp") then
			vim.lsp.handlers["textDocument/signatureHelp"] =
				vim.lsp.with(vim.lsp.handlers.signature_help, { border = "rounded" })
		end
		-- Remove the call to on_attach_signature_help
	end
	local server = require("lspconfig")[server_name]
	server.setup(opts)
end

return {
	"williamboman/mason-lspconfig.nvim",
	opts = {
		ensure_installed = {
			-- Makes sure Mason already have these installed
			-- "ruff-lsp",
			-- "rust_analyzer"
		},
	},
	{
		"neovim/nvim-lspconfig",
		dependencies = {
			-- Only needed for C++
			"p00f/clangd_extensions.nvim",
			init = function()
				require("lazyvim.util").lsp.on_attach(function(_, buffer)
					require("clangd_extensions.inlay_hints").setup_autocmd()
					require("clangd_extensions.inlay_hints").set_inlay_hints()
				end)
			end,
		},
		config = function()
			-- Set up all LSPs
			setup_lsp("ruff-lsp", {})
			setup_lsp("rust_analyzer", {})

			-- Add keybindings for Codeium LSP features
			vim.api.nvim_set_keymap(
				"n",
				"<leader>ca",
				"<cmd>lua vim.lsp.buf.code_action()<CR>",
				{ noremap = true, silent = true }
			)
			vim.api.nvim_set_keymap(
				"v",
				"<leader>ca",
				"<cmd>lua vim.lsp.buf.range_code_action()<CR>",
				{ noremap = true, silent = true }
			)
			vim.api.nvim_set_keymap(
				"n",
				"<leader>rn",
				"<cmd>lua vim.lsp.buf.rename()<CR>",
				{ noremap = true, silent = true }
			)
		end,
	},
}
