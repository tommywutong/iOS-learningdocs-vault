---
title: 'Friday Q&A 2015-09-18: Building a Gear Warning System'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-09-18-building-a-gear-warning-system.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d146e0f64ae4e4ab'
translated: false
---

> 原文：[Friday Q&A 2015-09-18: Building a Gear Warning System](https://www.mikeash.com/pyblog/friday-qa-2015-09-18-building-a-gear-warning-system.html)　·　mikeash.com Friday Q&A

Posted at 2015-09-18 13:29 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-11-06: Why is Swift's String API So Hard?](https://www.mikeash.com/pyblog/friday-qa-2015-11-06-why-is-swifts-string-api-so-hard.html)  
Previous article: [Friday Q&A 2015-09-04: Let's Build dispatch_queue](https://www.mikeash.com/pyblog/friday-qa-2015-09-04-lets-build-dispatch_queue.html)  
Tags: [arduino](https://www.mikeash.com/pyblog/?tag=arduino) [flying](https://www.mikeash.com/pyblog/?tag=flying) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [random](https://www.mikeash.com/pyblog/?tag=random)

Friday Q&A 2015-09-18: Building a Gear Warning System

by [Mike Ash](https://www.mikeash.com/)

**What Is This Thing?**  
I fly [gliders](https://www.mikeash.com/gliders.html). I own a share in a relatively high-performance single seat craft.

A glider's enemy is drag, and drag comes from sticking things out into the air. The glider needs a wheel for takeoff and landing, but that big wheel sticking out the bottom creates a lot of drag while flying. Because of this, a lot of gliders have retractable landing gear, including mine. Once I'm airborne and flying on my own, I pull a handle that raises the wheel into the body of the glider. Before landing, I push the handle back to the original position, which extends the wheel.

Every so often, that last part doesn't happen, and the glider lands on its belly. I've never done this and I hope I never will, but it's something that does happen. If you're fortunate enough to do this on grass, the damage can be pretty minimal, or even none. If you do it on a paved runway, the result is a long and expensive white stripe. This is not a good way to end your day.

To avoid this, it's nice to have something that can warn you if you go to land without lowering the landing gear. That's what I built.

**Basic Design**  
How do you actually detect when a pilot is landing with the gear up? Detecting whether the gear is up is relatively easy. You can install a microswitch somewhere in the retraction mechanism to detect its physical position, and you're all set.

Detecting "landing" is a bit harder. One possibility (which would be pretty fun to build) would be to use a GPS unit and terrain database (or at least an airport database) to detect when you're getting low. That's a lot of expense and complication I didn't need, though, and a nontrivial amount of power consumption as well.

The typical way to do this on a glider is to install a second microswitch that detects the position of the spoilers. Spoilers are big flat control surfaces that extend out the top of the wings to destroy the lift they produce and create drag. Drag is normally the enemy for a glider, but when landing drag can your friend. Gliders perform so well that it's extremely difficult to get them to come down at a reasonable rate when you want them to, so you use the spoilers to force a descent.

Spoilers are _typically_ used only for landing. This isn't always true. There are other scenarios where you want to descend rapidly, like if you find yourself above a scattered cloud deck that's closing up, but they're pretty rare. The spoiler position can be used as a pretty good "am I landing?" indicator. There will occasionally be false positives, but they're uncommon and can be tolerated.

The idea, then, is to install two microswitches, and sound the alarm whenever the spoilers are extended and the landing gear is not.

How exactly do you "sound the alarm"? I used a cheap, simple [piezo buzzer](http://www.radioshack.com/radioshack-6vdc-mini-buzzer/2730793.html) from RadioShack. It runs on almost no electricity and can be wired directly to a microcontroller's output pin. It's loud enough to be heard in flight (a glider cockpit is a pretty quiet place) without being annoyingly loud if it fires inadvertently.

**Hardware**  
The microswitches and buzzer would suffice on their own, with some wiring. Hook up the switches in series and have them pass current when in the alarm position. Wire the whole thing to some electricity, and the buzzer will buzz at the appropriate time. However, I wanted to use a microcontroller to drive everything for a few reasons:

1. A constant buzzing is not the most effective for getting someone's attention. Aviation is full of stories that go like, "What's that weird buzzing noise? Oh well, never mind that now, I have to land. _CRUNCH_" It happened to a friend of mine with one of these simple setups. A more complicated pattern stands a better chance of getting my attention.
2. There's a chance of hardware failure causing the system to get stuck in the alarm position. Having the alarm remain on for the entire flight afterwards would be extremely annoying. With a microcontroller, it can shut the warning off after a couple of minutes. In a situation where the warning is real, the pilot only has a couple of minutes to do something before it's too late anyway, so there's no need to keep it on longer than that.
3. It's a lot more fun.

For the microcontroller, I chose the [Digispark USB Development Board](http://digistump.com/products/1). It has a bunch of really nice features for this project:

1. It's cheap. The official price is $9, and I got it on sale for $6. If you're adventurous, you can pick them up on eBay for under $2.
2. It's easy. It works with the Arduino IDE which makes programming it really simple. It plugs directly into a USB port, so it doesn't need any special cables. Or even boring cables.
3. It has an on-board voltage regulator which accepts a wide range of voltages. This allows it to take power directly from my glider's main 12V batteries without needing any extra hardware to convert it.
4. It's really small, which is useful when I don't have a lot of room for the device.

It has some downsides as well compared to more typical Arduino hardware. Program memory is extremely limited at about 6kB, and it only has 6 IO pins. But it's more than enough for this project.

**Software Design**  
I have the Digispark run a loop that constantly polls the state of the microswitches. I could use interrupts instead, but since it has nothing else to do, a polling loop is easier. Power consumption is extremely low already, so there's no need to try to optimize this by sleeping the CPU.

When not in the alarm state, there's not much to do. The polling loop just ensures the buzzer isn't firing, and keeps checking.

When in the alarm state, it turns the buzzer on and off in a pattern. The pattern is fully programmable and needs to stop as soon as the microswitches change position. To make this happen, the buzzer pattern is stored as a sequence of bits in memory. When the buzzer starts, the current time is recorded. The time passed since that moment is used to look up the corresponding bit in the pattern, and the buzzer state is set to the value of that bit. A quick pulse of four buzzes would be recorded as `0xaa`, and a slower sequence of on and off would be `0xff 0x00 0xff 0x00 0xff 0x00 0xff`.

What exactly is the state we're looking for to sound the buzzer? Unfortunately, I was using switches that were already installed in the glider, and I couldn't remember how the switches were configured. Were they normally open or normally closed? What position activated them? I live a good distance from the airport, so it was inconvenient to go check. It needs to be configurable!

I thought about just baking it into the code and dragging my laptop out to the airport for the final setup. I thought about some sort of jumper configuration. But finally I settled on another plan.

I don't actually care how the switches are set up. There are four possible states the system can be in, and one of them is the state that sounds the alarm. But I don't care about the details of that state, or about the details of the other three.

I set up the system to watch another input pin. When that pin is pulled low (by shorting it to ground with some spare wire, for example), the system cycles through the four possible alarm states one per second. It saves the current state in the chip's onboard EEPROM, and loads that state when the program starts. To configure it, then, all I have to do is connect everything and put the aircraft into the alarm state while sitting on the ground. If the buzzer sounds, I'm all set. Otherwise, short the configuration pin to ground and wait for the buzzer to buzz. Once it does, remove the wire, and the correct configuration is saved.

**Code**  
Arduino is programmed in plain old C++ with some extra libraries available and some unusual entry points. The code should therefore be pretty easy to follow. Where something different is going on, I'll explain.

I'll start by defining some constants for the various IO pins. Arduino identifies pins by number, but I want better names for them, and the ability to easily change which pin a function is assigned to, in case I change the hardware:

```
    #define PIN_BUZZER 1
    #define PIN_ALERT_CONFIGURE 0
    #define PIN_GEAR 2
    #define PIN_SPOILER 5
```

The current configuration is stored in the low two bits of a global variable:

```
    int alertBits;
```

The low bit controls the gear, and the high bit controls the spoiler. When the bit is `0` the alert condition is for that pin to be low. When the bit is `1` the alert condition is for that pin to be high. I built two convenience functions to extract the bits and turn them into the Arduino constants `LOW` and `HIGH` which are returned from the function that reads a pin:

```
    int alertWhenGearIs() {
        return alertBits & 1 ? HIGH : LOW;
    }

    int alertWhenSpoilerIs() {
        return alertBits & 2 ? HIGH : LOW;
    }
```

The configuration is stored in the EEPROM. Data is stored in the EEPROM by address, starting from zero. I define a constant for the address that stores `alertBits`, although I just chose zero:

```
    #define ALERT_BITS_EEPROM_ADDRESS 0
```

When in configuration mode, the system will wait for a one second, then move to the next configuration. To do that, it needs to keep track of when the system entered configuration mode, which is done in a global variable:

```
    unsigned long alertConfigStartMillis;
```

On Arduino, an `int` is only 16 bits, which only gives a range of a little over a minute when storing milliseconds. `long` is 32 bits, which is about 49 days. Since this value will be populated with the number of milliseconds since startup, it's good to have it in a `long`. It could work as an `int` since it's only used to compute a delta for a short period of time, but it's better to use a data type big enough to hold the full value.

There's also a constant for how long to wait before moving to the next configuration. It waits for a thousand milliseconds:

```
    #define ALERT_CONFIG_DELAY_MILLIS 1000
```

It's useful to keep track of whether the system is currently buzzing, so that actions can be taken when moving between states. I define two states, and a variable to hold the current one:

```
    enum State {
        kIdle,
        kBuzzing
    };

    enum State state;
```

To know which bit to use in the alert pattern, the system needs to know when it went into the buzzing state, so it can compute how long it's been and figure out which bit is the current one. The start time is stored in another global:

```
    unsigned long buzzStartMillis;
```

The alert sound is stored as an array of bytes. I'll leave out the actual bytes for now:

```
    uint8_t alertSound[] = {
        ...
    };
```

The program needs to know how long each bit should be played for. I selected 62 milliseconds, which makes for about 16 bits per second. This is a good compromise betwen fine control over the timing and having the `alertSound` array be really long:

```
    #define MILLIS_PER_BIT 62
```

The Arduino environment automatically calls a function called `setup` when the program starts. This is a good place to do, well, setup:

```
    void setup() {
```

The various IO pins need to be configured. This is done by calling the built-in `pinMode` function and giving it a constant that indicates which mode to use for the pin in question. The buzzer pin is used as an output:

```
        pinMode(PIN_BUZZER, OUTPUT);
```

The gear pin is used as an input:

```
        pinMode(PIN_GEAR, INPUT);
```

The gear pin is also pulled high by enabling the internal pullup resistor. This is done by calling `digitalWrite` and setting it to `HIGH`. When the pin is configured as an output, this would cause the output to be high, but when it's an input it enables the pullup resistor instead:

```
        digitalWrite(PIN_GEAR, HIGH);
```

This means that if the switch is open, the input will be high. When the switch is closed, the input will be whatever the other side of the switch is connected to. I connected the switches to ground, which pulls the input low. This means that the wiring to the switches is all connected to ground, which made me slightly more comfortable than having them be powered all the time, although it really doesn't matter.

The spoiler pin is configured in the same way:

```
        pinMode(PIN_SPOILER, INPUT);
        digitalWrite(PIN_SPOILER, HIGH);
```

As is the configuration pin:

```
        pinMode(PIN_ALERT_CONFIGURE, INPUT);
        digitalWrite(PIN_ALERT_CONFIGURE, HIGH);
```

Finally, `alertBits` is loaded from the EEPROM. The value will normally be from zero to three, but it will be set to `255` the first time because that's the value for EEPROM locations that have never been written. Values out of the normal range are interpreted as zero. Data can be read from the EEPROM by calling `EEPROM.read`, which takes an EEPROM address and returns the value currently in it:

```
        int savedBits = EEPROM.read(ALERT_BITS_EEPROM_ADDRESS);
        alertBits = savedBits < 4 ? savedBits : 0;
    }
```

After the `setup` function completes, Arduino repeatedly calls the `loop` function until the power is cut. Ongoing code is placed here. The ongoing code has two tasks: check the gear and spoiler switches to sound the alarm when appropriate, and check the configuration pin to change the configuration when requested:

```
    void loop() {
        checkGearSpoiler();
        checkAlertConfig();
    }
```

Let's look at `checkGearSpoiler`:

```
    void checkGearSpoiler() {
```

The first thing to do here is to read current state of the switches. This is done by calling the `digitalRead` function:

```
        int gear = digitalRead(PIN_GEAR);
        int spoiler = digitalRead(PIN_SPOILER);
```

Then see if we should be sounding the buzzer. We sound the buzzer when both `gear` and `spoiler` are in the alert state:

```
        int soundBuzzer = (gear == alertWhenGearIs() &&
                           spoiler == alertWhenSpoilerIs());
```

If we're not sounding the buzzer, make sure `state` reflects that, and ensure the buzzer is turned off. This is done by using `digitalWrite` to set the buzzer pin to `LOW`:

```
        if(!soundBuzzer) {
            state = kIdle;
            digitalWrite(PIN_BUZZER, LOW);
```

Otherwise, we're in the alert state and we need to sound the buzzer according to the current position in the pattern.

```
        } else {
```

The first thing here is to get the current time. This is used to compute the current position in the buzzer pattern. The built-in function `millis` returns the number of milliseconds since startup:

```
            unsigned long now = millis();
```

If the current state is `kIdle` then we _just_ activated. Change the state, and set `buzzStartMillis` to the current time:

```
            if(state == kIdle) {
                state = kBuzzing;
                buzzStartMillis = now;
            }
```

To compute the current position in the pattern, we start by computing how much time has passed since we started the buzzer:

```
            unsigned long delta = now - buzzStartMillis;
```

The value to write to the buzzer pin (`LOW` or `HIGH`) will be stored in this local variable:

```
            int value;
```

Compute the current index in the pattern by dividing `delta` by the number of milliseconds per bit. Note that this is a _bitwise_ index, which will require some massaging to turn into an actual bit extracted from `alertSound`:

```
            unsigned long index = delta / MILLIS_PER_BIT;
```

It's possible we'll run off the end of the `alertSound` array. We don't want to start reading garbage, so if the index is off the end, we'll just set `value` to `LOW`:

```
            int soundBytes = sizeof(alertSound);
            int soundMax = soundBytes * 8;
            if(index >= soundMax) {
                value = LOW;
```

Otherwise, we need to extract the bit that corresponds to `index`. To do this, `index` has to be broken up into the index of the byte which contains the bit, and the index of the bit within that byte. This is done by dividing by 8 and using the quotient and remainder. Since this is a resource-constrained microcontroller, I did this with bitshifting (division by 8 is the same as `>> 3`) and masking (taking the remainder of dividing by 8 is the same as `& 0x07`), even though it surely doesn't matter in this particular case:

```
            } else {
                int byteIndex = index >> 3;
                int bitIndex = index & 0x07;
```

With the two indexes in hand, we can then get the byte out of `alertSound`, then shift and mask to get the bit we're after:

```
                uint8_t byte = alertSound[byteIndex];
                uint8_t bit = (byte >> bitIndex) & 0x01;
```

Then `value` is `HIGH` if the bit is set, otherwise it's `LOW`:

```
                value = bit ? HIGH : LOW;
            }
```

Finally, set the buzzer pin to whatever `value` was set to:

```
            digitalWrite(PIN_BUZZER, value);
        }
    }
```

That's all we need to play the buzzer pattern! This code runs repeatedly, and each time it retrieves the bit for the current moment in time and then either plays the buzzer or not. As long as it runs frequently, the result will be a nice pattern of buzzes. (And since this chip doesn't have much else to do, it should run very frequently indeed.)

Let's look at `checkAlertConfig` next:

```
    void checkAlertConfig() {
```

The first thing it does is, naturally, get the current state of the alert pin:

```
        int alertConfig = digitalRead(PIN_ALERT_CONFIGURE);
```

If the pin is `LOW` then we're in the configuration state:

```
        if(alertConfig == LOW) {
```

As before, the first thing here is to get the current time. This is used to advance to the next configuration state after the designated amount of time has passed:

```
            unsigned long now = millis();
```

Then it looks at `alertConfigStartMillis`, which holds the time when the program entered the configuration state. If it's zero then it just entered the configuration state, so it can be set to the current time:

```
            if(alertConfigStartMillis == 0) {
                alertConfigStartMillis = now;
```

Otherwise, compute the amount of time that has passed since the program entered the configuration state:

```
            } else {
                unsigned long delta = now - alertConfigStartMillis;
```

Then see if we've been in the configuration state long enough to move to the next state:

```
                if(delta >= ALERT_CONFIG_DELAY_MILLIS) {
```

If we are, increment `alertBits`, masking to just the bottom two bits to ensure it doesn't go beyond the 0-3 range:

```
                    alertBits = (alertBits + 1) & 3;
```

Then write this value to the EEPROM using `EEPROM.write`:

```
                    EEPROM.write(ALERT_BITS_EEPROM_ADDRESS, alertBits);
```

Finally, start a new configuration cycle by setting `alertConfigStartMillis` to `now`. This could cause some slop to accumulate in the timing, since it doesn't account for any extra time beyond when configuration started. But extreme precision isn't very accurate in this case, since configuration is only done once, and it's all human-driven anyway:

```
                    alertConfigStartMillis = now;
                }
            }
```

Finally, if the configuration pin isn't active, ensure that `alertConfigStartMillis` is zero so the program sees it when it does enter the configuration state:

```
        } else {
            alertConfigStartMillis = 0;
        }
    }
```

And that's it!

**Buzzer Pattern**  
For completeness, here is the full buzzer pattern I made for my unit. Since I made it so the pattern plays sixteen bits in one second, that means that two one-byte values make for one second. I formatted the array to put two values on each line, so each line is one second.

I constructed the pattern in a completely unscientific attempt to make something that would catch my attention even if distracted. I thought the key to this would be a lot of variation. It starts off with a rapid on/off pattern for one second. Then it pauses, then it plays a slower on/off pattern. Then there's a solid tone, in an attempt to say "PAY ATTENTION TO ME." Then I got creative and had it spell out GEAR UP and WARNING in Morse Code. I don't know Morse Code, but it stands out well. I end with a solid tone, and then if it still hasn't been fixed by then, the alert falls silent. Here's the full pattern:

```
    uint8_t alertSound[] = {
        // intermittent buzz for initial alert
        0xaa, 0xaa,

        // pause for a second
        0x00, 0x00,

        // steadier on/off sequence
        0xff, 0x00,
        0xff, 0x00,
        0xff, 0x00,
        0xff, 0x00,

        // pause for a second
        0x00, 0x00,

        // solid tone for two seconds
        0xff, 0xff,
        0xff, 0xff,

        // GEAR UP in morse code
        // --. . .- .-. / ..- .--.
        // 1110 1000  1000 1011
        // 1000 1011  1010 0000
        // 0010 1011  1000 1011
        // 1011 1010
        0xe8, 0x8b,
        0x8b, 0xa0,
        0x2b, 0x8b,
        0xba, 0x00,

        // repeat it a few times
        0xe8, 0x8b,
        0x8b, 0xa0,
        0x2b, 0x8b,
        0xba, 0x00,

        0xe8, 0x8b,
        0x8b, 0xa0,
        0x2b, 0x8b,
        0xba, 0x00,

        0xe8, 0x8b,
        0x8b, 0xa0,
        0x2b, 0x8b,
        0xba, 0x00,

        // WARNING in morse code
        // .-- .- .-. -. .. -. --.
        // 1011 1011  1000 1011
        // 1000 1011  1010 0011
        // 1010 0010  1000 1110
        // 1000 1110  1110 1000
        0xbb, 0x8b,
        0x8b, 0xa3,
        0xa2, 0x8e,
        0x8e, 0xe8,

        // then pause
        0x00, 0x00,

        // repeat that a few times too
        0xbb, 0x8b,
        0x8b, 0xa3,
        0xa2, 0x8e,
        0x8e, 0xe8,
        0x00, 0x00,

        0xbb, 0x8b,
        0x8b, 0xa3,
        0xa2, 0x8e,
        0x8e, 0xe8,
        0x00, 0x00,

        0xbb, 0x8b,
        0x8b, 0xa3,
        0xa2, 0x8e,
        0x8e, 0xe8,
        0x00, 0x00,

        // last ditch solid tone for ten seconds
        0xff, 0xff,
        0xff, 0xff,
        0xff, 0xff,
        0xff, 0xff,
        0xff, 0xff,
        0xff, 0xff,
        0xff, 0xff,
        0xff, 0xff,
        0xff, 0xff,
        0xff, 0xff,
    };
```

**CPU Speed**  
Power is at a premium in a glider. There's no way to generate electricity on board (some fancy people have solar cells, but I don't), so everything runs off batteries. I currently use a LiFePO4 battery with a capacity of 15Ah at about 13V. This has to power everything on board, including the power-hundgry transmitters in the VHF radio and radar transponder.

Compared to that, the power consumed by this processor is probably so small it can be ignored entirely. But it's still nice to get it as low as possible. The Digispark has the ability to reduce the CPU speed, which in turn makes it use substantially less power. The CPU is normally clocked to 16MHz, and reducing it to 1MHz makes it use 16x less power. 1MHz is still plenty fast for the small amount of work this program needs to do.

This isn't done in code, but is just a menu item in the Arduino IDE. When working on a project, you specify what kind of board it's for. With the Digispark, each available speed shows as a separate "board," so there's a Digispark entry for 16MHz, 8Mhz, and 1MHz. I just picked the last one, re-uploaded my program, and done!

**Conclusion**  
This was a fun project that was different from my usual Apple-related stuff. There wasn't anything too difficult about it, but it was nice to build something physical and practical. I put the end result in a small box and installed it behind my glider's instrument panel, where it lives right now, mostly doing nothing, and occasionally buzzing at me when I test it.

That's it for today! Come back next time for more exciting fun, probably back in the realm of Apple platforms. Friday Q&A is (mostly) driven by reader suggestions, so if you have an idea in the meantime of a topic you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

A quick note: I'm going to be traveling for a while soon, so my articles will be on hiatus until I'm back around the end of October. I hope to get one more article posted before I go, but no guarantees. Either way, don't worry, more will come soon!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-09-18-building-a-gear-warning-system.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
