---
title: XML-RPC and SOAP Programming Guide
apple_id: TP30001126
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/soapXMLRPC/chapter3/soapXMLRPC_scripts.html
archived_at: '2026-07-15T05:20:45.290614Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [XML-RPC and SOAP Programming Guide](Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md)


[Next](Making%20Remote%20Procedure%20Calls%20From%20Applications.md)[Previous](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md)

# Making Remote Procedure Calls From Scripts

Starting with OS X version 10.1, the Apple Event Manager provides support for using the XML-RPC and SOAP protocols to make remote procedure calls from AppleScript scripts and from applications. This chapter provides sample scripts that show how to make remote procedure calls from scripts.

This chapter assumes you are familiar with the material in [Introduction to XML-RPC and SOAP Programming Guide](Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temrnkrifqusfiyytami). To test any of the scripts shown in this chapter, you must have an Internet connection.

To make an XML-RPC request from a script, you use the AppleScript term `call xmlrpc`. The syntax for this term is described in [XML-RPC Script Statements](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temjnijauuq2cinbeu). You can find available XML-RPC services at sites such as XMethods at [http://www.xmethods.net/](http://www.xmethods.net/). There you can also find information about the parameters and return values for remote procedure calls to these services.

[Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temznijauuskeizeec) shows a script that prompts a user for text, makes an XML-RPC request to an Internet server to check the spelling for that text, prompts the user to correct any words that may have been misspelled, and displays the final text.

__Listing 2-1__  A script that makes an XML-RPC request to check the spelling of a text phrase.

```
---- Main script ----------------------------------------
-- Supply default text to spell check.
set spellCheckText to "My frst naem is John"

----Query user for different text to check.
set dialogResult to display dialog ¬
    "Enter a phrase to spell check:" default answer spellCheckText

if button returned of dialogResult is "OK" then
    set spellCheckText to text returned of dialogResult
    -- Call spellCheck handler.
    set resultList to spellCheck(spellCheckText)
    (*
    The returned data looks something like this:
        {{suggestions:{"fast", "fest", "first", "fist", "Forst",
        "frat", "fret", "frist", "frit", "frost", "frot", "fust"},
        location:4, |word|:"frst"}, {suggestions:{"haem", "na em",
        "na-em", "naam", "nae", "nae m", "nae-m", "nael", "Naim",
        "nam", "name", "neem"}, location:9, |word|:"naem"}}
    *)
    -- Make list of words to spellcheck.
    set wordList to every word of spellCheckText

    -- Give user chance to correct each misspelled word.
    repeat with eachItem in resultList
        set newWord to choose from list suggestions of eachItem ¬
            with prompt "You misspelled \"" & |word| of eachItem & ¬
            "\"" without multiple selections allowed

        -- If user selected a corrected word, insert it into list
        if (newWord as string) is not equal to "false" then
            set wordIndex to ¬
                findIt(every word of spellCheckText, location of eachItem)
            copy newWord to item wordIndex of wordList
        end if
    end repeat

    -- Display corrected text.
    set spellCheckText to ""
    repeat with oneWord in wordList
        set spellCheckText to spellCheckText & oneWord & " "
    end repeat

    display dialog "Corrected text: " & spellCheckText
end if

-- spellCheck handler ------------------------------------------
-- This handler makes the remote procedure call.
on spellCheck(sentence)
    tell application "http://www.stuffeddog.com/speller/speller-rpc.cgi"
        return call xmlrpc {method name:"speller.spellCheck", ¬
        parameters:sentence}
    end tell
end spellCheck


-- findIt handler ------------------------------------
-- The "textList" parameter is a list of the words in the original text.
-- The "index" parameter is the character index of a misspelled word.
-- This handler returns the word at that index.
-- For example, the misspelled word at character index four is "frst".
--      Its word index is 2 (the 2nd word in the original text).
on findIt(textList, index)
    set curLength to 0
    set ixWord to 1

    repeat with oneWord in textList
        set curLength to curLength + (length of oneWord) + 1
        if curLength ≥ index then
            exit repeat
        end if
        set ixWord to ixWord + 1
    end repeat
    log ixWord
    return ixWord
end findIt
```

This script has a main section and two handlers. In the main section, it performs the following actions:

1. It sets a default text string to be checked.
2. It displays a dialog that prompts the user to enter different text.
3. If the user accepts the dialog, it calls the `spellCheck` handler to check the spelling. That handler, described below, contains the only script statements needed to make a remote procedure call to a spell-checking server.

   The handler returns a list that contains, for each misspelled word, a list of suggested corrections, the character location of the word in the text, and the misspelled word itself. The returned list looks something like this:

```
The returned data looks something like this:
        {{suggestions:{"fast", "fest", "first", "fist", "Forst",
        "frat", "fret", "frist", "frit", "frost", "frot", "fust"},
        location:4, |word|:"frst"}, {suggestions:{"haem", "na em",
        "na-em", "naam", "nae", "nae m", "nae-m", "nael", "Naim",
        "nam", "name", "neem"}, location:9, |word|:"naem"}}
```

   Note that this is not the raw data returned from the remote procedure call. Rather, the Apple Event Manager has interpreted the XML returned by the procedure call and built an Apple event to encapsulate it. This list of records is the result. Because `word` is a reserved word in AppleScript, it is enclosed in vertical bars (`|word|`) when used as an identifier (in this case as a label in a record).
4. For each word (if any) in the returned list of misspelled words, it lets the user choose a correction (using the standard scripting addition `choose from list`).

   It then calls the `findIt` handler to find the location of the misspelled word in the text phrase and replaces it with the user choice.
5. It displays the corrected text (possibly the same as the original text, if no corrections were made).

The `spellCheck` handler contains the one and only statement in the script that makes a remote procedure call. It performs the following operations:

1. It uses a Tell statement to identify the location of the remote XML-RPC server (`http://www.stuffeddog.com/speller/speller-rpc.cgi`).
2. It uses the AppleScript term `call xmlrpc` to make the remote procedure call, specifying the method name (`speller.spellCheck`) and passing the specified text for the single parameter.
3. It returns the result of the remote procedure call. That consists of a list that contains, for each misspelled word, a list of suggested corrections, the location of the word in the text, and the misspelled word itself.

Note that AppleScript, working through the Apple Event Manager, did all the work of formatting the `call xmlrpc` script statement into proper XML, opening a connection to the specified server, sending the message, waiting for a reply, formatting the returned XML into an Apple event, and returning the event.

The `findIt` handler merely returns the word position in the original text of the word that corresponds to the passed character index of a misspelled word (returned by the remote procedure handler). For example, the character index of the first misspelled word (`frst`) is 4. That word is the second word in the original text, so `findit` would return the value 2.

For a script that shows a more flexible type of handler and includes error handling, see [Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temznijauurceifaus).

To make a SOAP request from a script, you use the AppleScript term `call soap`. The syntax for these calls is described in [SOAP Script Statements](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temjnijauur2iirbuq). You can find available SOAP services at sites such as XMethods at [http://www.xmethods.net/](http://www.xmethods.net/). There you can also find information about the parameters and return values for SOAP requests to these services.

[Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temznijauur2bireug) shows a script that prompts a user for text, makes a SOAP request to an Internet server to translate that text to French, and displays the translated text.

__Listing 2-2__  A simple script that calls a SOAP translation server.

```
---- Main script ----------------------------------------
-- Supply default text to translate.
set defaultText to "The spirit is willing but the mind is weak"

--Display dialog and let user type different text to translate.
display dialog "Enter the text to translate into French:" ¬
    default answer defaultText
set this_text to the text returned of the result

-- Call translation handler
set the new_text to translate("en_fr", this_text)

--Show translated text and allow user to copy it to Clipboard.
display dialog new_text buttons {"Clipboard", "OK"} default button 2
if the button returned of the result is "Clipboard" then
    set the clipboard to new_text
end if

-- translate handler ------------------------------------------
-- This handler makes the SOAP request.
on translate(direction, theText)
    tell application "http://services.xmethods.net:80/perl/soaplite.cgi"
        return call soap {method name:"BabelFish", ¬
        method namespace uri:"urn:xmethodsBabelFish", ¬
        parameters:{translationmode:direction as string, ¬
        sourcedata:theText as string}, ¬
        SOAPAction:"urn:xmethodsBabelFish#BabelFish"}
    end tell
end translate
```

This script starts has a main section and one handler to make the translation SOAP request. In the main section, it performs the following actions:

1. It sets a default text string to be translated from English to French.
2. It displays a dialog that prompts the user to enter different text.
3. It calls the `translate` handler to translate the text. That handler, described below, contains the only script statements needed to make a SOAP request to a translation server.

   The handler returns the translated text.
4. It displays the translated text and allows the user to copy it to the Clipboard.

The `translate` handler contains the one and only statement in the script that makes a SOAP request. It performs the following operations:

1. It uses a Tell statement to identify the location of the remote SOAP server (`http://services.xmethods.net:80/perl/soaplite.cgi`).
2. It uses the AppleScript term `call soap` to make the SOAP request. You can obtain certain values you need to make a SOAP request from the service itself. In this example, the call includes the following:

   - `method name:"BabelFish"` specifies the required method name
   - `method namespace uri:"urn:xmethodsBabelFish"` specifies the required method namespace URI
   - `parameters:{translationmode:direction as string, sourcedata:theText as string}` specifies the parameter names and the values to pass for those parameters; a method may have no parameters
   - `SOAPAction:"urn:xmethodsBabelFish#BabelFish"` specifies the required SOAPAction value
3. It returns the result of the SOAP request. That consists of a text string that contains the translated text.

Note that AppleScript, working through the Apple Event Manager, did all the work of formatting the `call soap` script statement into proper XML, opening a connection to the specified server, sending the message, waiting for a reply, formatting the returned XML into an Apple event, and returning the event.

The script in [Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temznijauurceifaus) performs the same task as the script in [Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temznijauur2bireug), translating an English phrase to French. However, it is more flexible and sophisticated in several ways:

1. It turns the translation handler into a flexible SOAP request routine that can call different SOAP servers and different methods depending on the parameters passed to it.
2. It uses error handling in the SOAP request handler and sets a boolean parameter value so that the caller can check for success. The main script checks that parameter and displays an error message if the SOAP request was unsuccessful.
3. The main script also shows how to use a `try` block to handle errors. In this case, it checks for errors while displaying a dialog: for any returned error number except -128 (the user cancelled), it beeps.
4. It defines property values to make the script more readable and easier to modify.

__Listing 2-3__  A more detailed script that calls a SOAP translation server.

```
-- Use properties to store default values.
property SOAP_app : "http://services.xmethods.net:80/perl/soaplite.cgi"
property method_name : "BabelFish"
property method_namespace_URI : "urn:xmethodsBabelFish"
property SOAP_action : "urn:xmethodsBabelFish#BabelFish"
property English_to_French : "en_fr"

---- Main script ----------------------------------------
--Query user for text to translate.
set this_text to "Hello my friend!"
repeat
    try
        display dialog ¬
            "Enter the text to translate into French:" ¬
            default answer this_text
        set this_text to the text returned of the result
        if this_text is not "" then
            set this_text to this_text as string
            exit repeat
        end if
    on error number error_number
        -- Don't show error if user just cancelled.
        if the error_number is -128 then error number -128
        beep
    end try
end repeat

-- Create the parameter record.
set the method_parameters to {translationmode:English_to_French, ¬
     sourcedata:this_text}

-- Call the SOAP handler.
copy my SOAP_call(SOAP_app, method_name, ¬
    method_namespace_URI, method_parameters, SOAP_action) ¬
    to {call_indicator, call_result}

-- Check for error return from SOAP handler.
if the call_indicator is false then
    beep
    display dialog "An error occurred." & return & return ¬
        & call_result buttons {"Cancel"} default button 1
else
    --Show translated text and allow user to copy it to Clipboard.
    display dialog call_result buttons {"Clipboard", "OK"} ¬
        default button 2
    if the button returned of the result is "Clipboard" then
        set the clipboard to the call_result
    end if
end if

-- SOAP translation handler ------------------------------
on SOAP_call(SOAP_app, method_name, ¬
    method_namespace_URI, method_parameters, SOAP_action)
    try
        using terms from application "http://www.apple.com/placebo"
            tell application SOAP_app
                set this_result to call soap ¬
                    {method name:method_name ¬
                        , method namespace uri:method_namespace_URI ¬
                        , parameters:method_parameters ¬
                        , SOAPAction:SOAP_action}
            end tell
        end using terms from
        return {true, this_result}
    on error error_message
        return {false, error_message}
    end try
end SOAP_call
```

[Next](Making%20Remote%20Procedure%20Calls%20From%20Applications.md)[Previous](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md)

