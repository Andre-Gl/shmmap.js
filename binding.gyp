{
	"targets": [
		{
			"target_name": "shmmap",
			"conditions":[
				["OS=='mac'", {
					"sources": [ "src/memory_mac.cpp" ],
				}],
				["OS=='linux'", {
					"sources": [ "src/memory_linux.cpp" ],
				}],
				["OS=='win'", {
					"sources": [ "src/memory_win.cpp" ],
				}],
			],
			"include_dirs": [
				"<!(node -e \"require('nan')\")"
			]
		}
	]
}
