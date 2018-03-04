{
    "targets": [
        {
            "target_name": "my_lcd",
            "sources": [
                "obj/ddmain.cc"],
            "include_dirs": [ "<!(node -e \"require('nan')\")" ],
            'libraries': [
                '-L/usr/local/lib', '-lwiringPi'
            ]
        }
    ]
}
