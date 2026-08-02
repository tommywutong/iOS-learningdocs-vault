---
title: Preferences Programming Topics for Core Foundation
apple_id: 10000129i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/Tasks/UsingHighAPI.html
archived_at: '2026-07-15T07:22:44.650547Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preferences Programming Topics for Core Foundation](Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Using%20the%20Low-Level%20Preferences%20API.md)[Previous](Preference%20Domains.md)

# Using the High-Level Preferences API

The functions [CFPreferencesSetAppValue](https://developer.apple.com/documentation/corefoundation/1515528-cfpreferencessetappvalue) and [CFPreferencesCopyAppValue](https://developer.apple.com/documentation/corefoundation/1515497-cfpreferencescopyappvalue) are the most straightforward way for an application to create and retrieve a preference that is specific to the current user and application. The preference data is written to the default domain (Current User, Current Application, Any Host) and so it will be available on all machines that this user can log into. These functions should never be called with `kCFPreferencesAnyApplication`, only a true application ID or `kCFPreferencesCurrentApplication`.

Preferences are stored as key/value pairs. The key must be a CFString object, but the value can be any Core Foundation property list value (see _[Property List Programming Topics for Core Foundation](../Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i)_), including the container types. For example, you might have a key called `defaultWindowWidth` which defines the width in pixels of any new windows that your application creates. Its value would most likely be of type CFNumber. You might also decide to combine window width and height into a single preference called `defaultWindowSize` and make its value be a CFArray object containing two CFNumber objects.

The code in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dslkciffeeskjizdq) demonstrates how to create a simple preference for the application “MyTextEditor”. The example sets the default text color for the application to blue.

__Listing 1__  Writing a simple default

```
CFStringRef textColorKey = CFSTR("defaultTextColor");
CFStringRef colorBLUE = CFSTR("BLUE");

// Set up the preference.
CFPreferencesSetAppValue(textColorKey, colorBLUE,
        kCFPreferencesCurrentApplication);

// Write out the preference data.
CFPreferencesAppSynchronize(kCFPreferencesCurrentApplication);
```

Notice that `CFPreferencesSetAppValue` by itself is not sufficient to create the new preference. A call to `CFPreferencesAppSynchronize` is required to actually save the value. If you are writing multiple preferences, it is more efficient to sync only once after the last value has been set than to sync after each individual value is set. For example, if you implement a preference panel you might only synchronize when the user presses an “OK” button. In other cases you might not want to sync at all until the application quits—although note that, of course, if the application crashes all unsaved preferences settings will be lost.

The simplest way to locate and retrieve a preference value is to use the `CFPreferencesCopyAppValue` function. This call searches through the various preference domains in order until it finds the key you have specified. If a preference has been set in a less-specific domain—”Any Application”, for example —its value will be retrieved with this call if a more specific version cannot be found. [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dslkcineuiqseifda) shows how to retrieve the text color preference saved in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dslkciffeeskjizdq).

__Listing 2__  Reading a simple default

```
CFStringRef textColorKey = CFSTR("defaultTextColor");
CFStringRef textColor;

// Read the preference.
textColor = (CFStringRef)CFPreferencesCopyAppValue(textColorKey,
        kCFPreferencesCurrentApplication);
// When finished with value, you must release it
// CFRelease(textColor);
```

Note that all values returned from preferences are immutable, even if you have just set the value using a mutable object.

An example of simple preference updating is a game that searches for a high score preference each time a round is completed. If there is no high score preference, the application writes the current score as the high score. If a high score preference exists, it is compared with the new score and updated if the new score is higher. [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dslkcineuiqkkifdq) demonstrates this process.

__Listing 3__  Updating a preference

```
CFStringRef highScoreKey = CFSTR("High Score");
CFNumberRef tempScore;
int highScore;

// Look for the preference.
tempScore = (CFNumberRef)CFPreferencesCopyAppValue(highScoreKey,
        kCFPreferencesCurrentApplication);

// If the preference exists, update it. If not, create it.
if (tempScore)
{
    // Numbers come out of preferences as CFNumber objects.
    if (!CFNumberGetValue(tempScore, kCFNumberIntType, &highScore)) {
        highScore = 0;
    }
    CFRelease(tempScore);

    printf("The old high score was %d.", highScore);
}
else
{
    // No previous value.
    printf("There is no old high score.");
    highScore = 0;
}

highScore += 5;

// Create the CFNumber to pass to the preference API.
tempScore = CFNumberCreate(NULL, kCFNumberIntType, &highScore);

// Set the preference value, or update it if it already exists.
CFPreferencesSetAppValue(highScoreKey, tempScore,
        kCFPreferencesCurrentApplication);

// Release the CFNumber.
CFRelease(tempScore);

// Write out the preferences.
CFPreferencesAppSynchronize(kCFPreferencesCurrentApplication);
```

The technique shown in [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dslkcineuiqkkifdq) generalizes to context of multiple preferences where an application tries to locate a set of preferences for display to the user in a graphical preference panel. If no preferences exist, default values are used. If existing preference values are found, they are used to initialize the preference panel for display to the user. After the user makes changes and pushes the “OK” button, you can set the changed preference values and write them to storage.

[Next](Using%20the%20Low-Level%20Preferences%20API.md)[Previous](Preference%20Domains.md)

