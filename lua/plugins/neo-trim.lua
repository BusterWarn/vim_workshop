return {
	"BusterWarn/neo-trim",
	config = function()
		require("neo-trim").setup({
			auto_trim_on_write = true,
			exclude_diagnostics_for_languages = { "lua" }, -- File types to exclude from diagnostics
			exclude_auto_trimming_for_languages = { "lua" }, -- File types to exclude from automatic trimming
		})
	end,
}
