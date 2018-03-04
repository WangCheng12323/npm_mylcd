{
    "targets": [
        {
            "target_name": "mylcd_rpi",
            "sources": [
                "obj/main.c"],
            "include_dirs": ["<!(node -e \"require('nan')\")"],
            'libraries': [
                '-L/usr/local/lib', '-lwiringPi'
            ]
        }
    ]
}
