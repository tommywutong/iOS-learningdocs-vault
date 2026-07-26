---
title: How to fix malfunctioning AirPods
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2023/11/14/fix-airpods-reset/'
original_language: en
published: 2023-11-14
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6b682b66a3a2b1ab'
translated: false
---

> 原文：[How to fix malfunctioning AirPods](https://www.jessesquires.com/blog/2023/11/14/fix-airpods-reset/)　·　Jesse Squires

A few weeks ago my AirPods Pro 2 (with Lightning, not USB-C) suddenly started acting buggy and weird. The case no longer made the chime sound when plugging them in to charge. I stopped getting “Left Behind” notifications from the Find My app. After updating to iOS 17, I could not get them to install [the latest firmware](https://www.macrumors.com/2023/11/09/airpods-pro-2-firmware-6b32/), which enables the new features for Adaptive Audio, Conversation Awareness, and Personalized Volume. I had been trying for weeks to [follow the magic steps that will trigger a firmware update](https://www.macrumors.com/how-to/update-airpods/) with no luck. Even worse, after a full charge of both the AirPods and the case, the batteries for all of them would drain to zero percent within 2-3 days.

I have no idea what triggered all of these issues, but my current theory is that I interrupted a firmware update that put them in an inconsistent state. But, who knows. In any case, I’m happy to report that a hard reset seems to have fixed all of these problems! If you’ve been experiencing any of these (or similar) issues with your AirPods, you should try resetting them.

I found [this support guide from Apple](https://support.apple.com/en-us/HT209463) on how to reset your AirPods, which states _“You might need to reset your AirPods if they won’t charge, or to fix a different issue.”_ It isn’t clear to me exactly what resetting does — aside from the obvious steps of completely unpairing them, removing them from your iCloud account, forgetting them in your Bluetooth settings, and then repairing them. I suspect it might also restore the last-known good firmware?

Here are the steps [from the support guide](https://support.apple.com/en-us/HT209463):

> 1. Put your AirPods in their charging case, and close the lid.
> 2. Wait 30 seconds.
> 3. Open the lid of your charging case, and put your AirPods in your ears.
> 4. Go to Settings \> Bluetooth. Or go to Settings \> [your AirPods].
> 5. If your AirPods appear there as connected, tap the More Info button next to your AirPods, tap Forget This Device, then tap again to confirm.
> 6. If your AirPods don’t appear there, continue to the next step.
> 7. Put your AirPods in their charging case, and keep the lid open.
> 8. Press and hold the setup button on the back of the case for about 15 seconds, until the status light on the front of the case flashes amber, then white.
> 9. Reconnect your AirPods: With your AirPods in their charging case and the lid open, place your AirPods close to your iPhone or iPad. Follow the steps on your device’s screen.

Note that on step (8), it took longer than 15 seconds for me. It was more like 30 seconds. The light on the case was initially white, and _then_ amber, then white again. Make sure you hold the button until you see the amber light, and then white.

After following these steps, I then tried to [trigger a firmware update](https://www.macrumors.com/how-to/update-airpods/) following the random magic steps that people have experimented with to make this happen implicitly. I wish Apple would just add an “Update Firmware” button in the Settings! Anyway — the firmware update installed successfully almost immediately and the case even chimed after it completed!

As far as I can tell, my AirPods are as good as new.
