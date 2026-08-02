---
title: AppleScript Language Guide
apple_id: TP40000983
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-01-25'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_load_script.html
archived_at: '2026-07-15T05:19:32.668550Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Language Guide](Introduction%20to%20AppleScript%20Language%20Guide.md)


[Next](Unsupported%20Terms.md)[Previous](Double%20Angle%20Brackets.md)

# Libraries using Load Script

OS X Mavericks v10.9 (AppleScript 2.3) introduces built-in support for script libraries, which are scripts containing handlers that may be shared among many scripts. Scripts that must run on older versions of the OS can share handlers between scripts using `load script`, as described here.

In addition to defining and calling handlers within a script, you can access handlers from other scripts. To make a handler available to another script, save it as a compiled script, then use the `[load script](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvztgu)` command to load it in any script that needs to call the handler. You can use this technique to create libraries containing many handlers.

For example, the following script contains two handlers: `areaOfCircle` and `factorial`:

```
-- This handler computes the area of a circle from its radius.
-- (The area of a circle is equal to pi times its radius squared.)
on areaOfCircle from radius
    -- Make sure the parameter is a real number or an integer.
    if class of radius is contained by {integer, real}
        return radius * radius * pi -- pi is predefined by AppleScript.
    else
        error "The parameter must be a real number or an integer"
    end if
end areaOfCircle


-- This handler returns the factorial of a number.
on factorial(x)
    set returnVal to 1
    if x > 1 then
        repeat with n from 2 to x
            set returnVal to returnVal * n
        end repeat
    end if
    return returnVal
end factorial
```

In Script Editor, save the script as a compiled Script (which has extension `scpt`) or Script Bundle (extension `scptd`) and name it “NumberLib”.

After saving the script as a compiled script, other scripts can use the `load script` command to load it. For example, the following script loads the compiled script `NumberLib.scpt`, storing the resulting `script` object in the variable `numberLib`. It then makes handler calls within a `tell` statement that targets the `script` object. The compiled script must exist in the specified location for this script to work.

```
set numberLibrary to (load script file "NumberLib.scpt")

tell numberLibrary
    factorial(10)             --result: 3628800
    areaOfCircle from 12      --result: 452.38934211693
end tell
```

[Next](Unsupported%20Terms.md)[Previous](Double%20Angle%20Brackets.md)

