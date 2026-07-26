---
title: Apple Watch, One Year In
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/04/apple-watch-thoughts/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:17edf9276906a4bf'
translated: false
---

> 原文：[Apple Watch, One Year In](https://oleb.net/blog/2016/04/apple-watch-thoughts/)　·　Ole Begemann

# Apple Watch, One Year In

[![Press image of several Apple Watch models](https://oleb.net/media/apple-watches-marketing-image.jpg)](https://oleb.net/media/apple-watches-marketing-image.jpg)

I’ve worn [my Apple Watch](http://www.apple.com/watch/gallery/#/42/space-gray-aluminum-case/black-sport-band) every single day since I got it in May 2015. Despite its many problems, the watch has quickly become a device for me that I don’t want to miss anymore. The main, and perhaps only, reason for this is the activity tracking.

# Activity tracking

The Activity app on the watch and on the iPhone breaks down your daily activity into three metrics:

1. _Stand_: stand up and walk around for at least 1 minute in at least 12 hours of the day.
2. _Exercise_: get your heart rate elevated for at least 30 minutes every day. Anything that brings up your heart rate to more than about 100 beats per minute counts as exercise. For me, a brisk walk does it. You don’t have to start an explicit workout to fill up your exercise ring.
3. _Move_: reach your daily “active calories” goal, i.e. the calories you burn on top of your [basal metabolic rate](https://en.wikipedia.org/wiki/Basal_metabolic_rate), which represents the calories you would expend if you lay motionless in bed all day. Unlike the other two metrics, you can set the amount of calories that counts as an achievement for this goal yourself.^[1](#fn:1) This is obviously not an exact science, but that doesn’t matter. The calorie measurements don’t have to be very accurate to be useful (and I have no way of verifying whether they are^[2](#fn:2)), they just have to consistent from day to day.

In addition, the Activity app will award you badges for certain achievements, such as doubling your _Move_ goal or having a perfect week or month (reaching your _Move_ goal every single day of a month). The gamification aspect is very simple, and I don’t know if the system is the result of years of highly scientific experiments by Apple to achieve the perfect balance between motivation, simplicity, and inconvenience, or if it’s just a lucky strike. All I can say is that it works extremely well for me. Getting perfect months and not breaking a long streak has become a little addictive — at times even to the point where it may actually be counterproductive because rest days are important, too.^[3](#fn:3)

Activity tracking with the Apple Watch has turned me into someone who cares about daily exercise, and it helped me lose a significant amount of weight over the last year. That alone is reason enough for me to wear the watch every day.

# Everything else I do with the Apple Watch

I settled on the Modular watch face with these [complications](https://developer.apple.com/watch/human-interface-guidelines/app-components/#complications): Activity, Date, Weather, Battery. I like the designs for the watch faces, although I hope there will be much more variety in the future. Complications are a great feature and I’m glad Apple has allowed developers to offer complications. As so many other things on the the watch, many third-party complications suffer from infrequent update intervals imposed by the OS in order to conserve battery life.

[Notifications](https://developer.apple.com/watch/human-interface-guidelines/app-components/#notifications) are nice but not essential for me. I just don’t get many that require immediate attention. The haptic feedback is fantastic, though. So much better than vibration or sound. After a while it’s easy to distinguish the different tap patterns. To get the most out of haptic feedback, I found it helpful to disable it for all but the most important notification types. For example, I don’t need to know immediately when an email arrives. It’s enough to see the red notification dot the next time I look at the watch.

The only [glance](https://developer.apple.com/watch/human-interface-guidelines/app-components/#glances) I use regularly is [Now Playing](http://www.macworld.com/article/2987673/streaming-media/the-different-ways-to-play-music-on-an-apple-watch.html), but that one is extremely convenient. I mainly use it at home to control my iPhone playing over a Bluetooth speaker.

Battery life is good enough if you charge daily. I have about 50% of battery left on most days. Long workout sessions can deplete the battery in a few hours, caused (I think) by the near-continuous heart rate monitoring. This becomes a problem on a 3–4+ hour bike ride, not on an hour-long run. The battery charges quickly, so if you want to use the watch to track your sleep (e.g. with [Sleep++](https://david-smith.org/apps/)), charging it for an hour or so in the morning or evening is sufficient.

I disabled the passcode protection on the watch several months ago. I like not having to enter it very much, and I don’t think there’s much of a downside. Apple Pay is not available in Germany, there isn’t really a lot sensitive information on the watch when it’s not connected to my iPhone, and the likelihood that I lose it or it gets stolen is pretty small.

# Looks

The Apple Watch looks better than most (all?) other smartwatches out there in my opinion. I can’t say I love the design, though. I’d much rather wear a traditional watch if it were just about looks. That’s not even due to the particular design of the current model (which is fine in my opinion), so I’m not sure Apple can do much about it.

Wearing a watch is a fashion statement. The Apple Watch screams “smartwatch” to me, putting its wearer automatically — justified or not — into the nerd category. I’m not particularly comfortable with that for myself. (Although I unquestionably am one.) Moreover, Apple’s huge popularity means that many people can readily identify the watch as an Apple product. Wearing an Apple Watch in 2015/2016 inevitably (I think) pigeonholes a person as an avid Apple fan, and I’m not comfortable with that characterization, either.

I’m sure some of my uneasiness will disappear over time as smartwatches get more popular, but given that I feel the same way about the blatantly obtrusive Apple logo on my laptop and that I try to avoid visible logos on my shoes and clothing as much as possible, I doubt it will ever go away.^[4](#fn:4) I just don’t want to be a walking advertisement for the products I use, and/or have everybody know how much I paid for them (especially if they were expensive). That is a significant downside to any wearable Apple product for the foreseeable future for me.

The sport band is comfortable and of a very high quality. I haven’t gotten any additional bands yet, mainly because I find Apple’s other bands too expensive. I like the [link bracelet](http://www.apple.com/watch/gallery/#/42/stainless-steel-case/link-bracelet) and [classic buckle](http://www.apple.com/watch/gallery/#/42/stainless-steel-case/marigold-classic-buckle), though. I ordered one of the new [nylon bands](http://www.apple.com/watch/gallery/#/42/space-gray-aluminum-case/gold-royal-blue-woven-nylon), but it hasn’t arrived yet.

The build quality of the Apple Watch is really nice. My “cheap” aluminum model looks as good as new, and I haven’t taken special care to protect it.

# Apps

As many others have written, apps on the Apple Watch suffer from unbearably slow load times. It’s not uncommon to launch an app and see nothing but a spinner for the 7 seconds or so before the screen turns off again. Native watchOS 2 apps were promised to be faster, though I can’t really tell the difference. Some of this may be due to developers not being familiar enough with the platform, but since even [the most simple apps take about 5 seconds to launch](https://twitter.com/chockenberry/status/725094375970103296), I’m inclined to blame it on the hardware or the OS. If Samsung had shipped a product that worked like this, I think the Apple community would ridicule them pretty harshly for it.

Combine the load times with Apple’s (sensible) recommendation that good watch apps have interaction times of 5 seconds or less and you’ll end up with few truly useful watch apps at the moment.

However, I do think there are some areas where apps make sense, even under the current limitations. I like David Smith’s take on this in [Watch Apps Worth Making](https://david-smith.org/blog/2016/02/12/watch-apps-worth-making/): if your app can provide rich notifications or complications, it can provide a lot of value, even if users never launch the actual app. The other area David mentions is apps that utilize the watch’s sensors. His app [Sleep++](https://david-smith.org/apps/) is a perfect example of this. Workout-related apps can also be great because they are typically used in situations when using your smartphone is not practical. For instance, [Gymaholic](https://gymaholic.me) allows you to track a gym workout on the watch. And because the app remains active during the workout, you only have to suffer the load time once.

# What I don’t like

- Speed, speed, speed. I hope the Apple Watch 2 or 3 will be much faster.
- Apple doesn’t guarantee waterproofness, but I’ve worn the watch dozens of times under the shower without any problems. Unfortunately, the touchscreen quickly becomes unusable when it comes into contact with water. This is a major problem for me in the [Workout app](https://support.apple.com/en-us/HT204523) because rain or sweaty fingers can make it almost impossible to swipe between screens or to simply end the workout. I’m not sure if Apple can do anything about this by using different hardware. Capacitive touchscreens may always have a problem with water.
- The information density in the Workout app (one of my most used apps) is way too low. The app only displays two pieces of information at once during a workout (one of elapsed time, speed/pace, distance, active calories, total calories, and heart rate; and one of time of day, elapsed time, and speed). Who wants to swipe multiple times during a run, especially when a tiny amount of sweat can make the touchscreen inoperative?

  Swiping is just as bad during cycling. Unless you want to cycle hands-free, you have to leave your watch hand on the handlebars and use the other hand to operate touch the screen. If all the information were on a single screen, you could just raise your wrist.

  The screen is big enough to display at least four items at once. Considering that no one needs to see both active and total calories, I bet you could fit all relevant information on a single screen.
- The side button, reserved for contacting your twelve favorite friends, is almost useless to me. In fact, the most use I get out of the side button is to [make screenshots](https://support.apple.com/en-us/HT204673) and to [kill an app](http://www.imore.com/how-force-quit-apps-apple-watch) when it won’t launch (which happens regularly). I hope we’ll be able to use it for more things in the future. For example, it would be perfect for pausing and resuming a workout without having to fiddle with the touchscreen. I never wanted to quickly contact a friend during a workout. And if it’s possible to tell Siri to pause or stop a workout, I haven’t found the magic incantation yet.
- The watch/iPhone combo doesn’t recognize you’re cycling unless you explicitly start a cycling workout.
- The hourly stand notifications (10 minutes before the hour when you have sat the whole time) is too intrusive. I don’t want to turn them off because I appreciate the reminder, but I don’t need to read the same “Time to stand” notification text (and then have to dismiss it) for the umpteenth time. I’d much rather characteristic double tap, and when I raise my wrist in response to that, just flash the stand ring in the activity complication.
- Activating the screen by raising your wrist works almost all the time. Especially when lying down it’s quite unreliable, though. The fact that the screen is not always on is a problem anyway: you can’t glance at your watch without raising your wrist. On the other hand, an always-on screen that emits light would be very annoying in dark rooms. I hope Apple finds a good solution for both problems.
- Configuring the watch via the iPhone app is frustrating. Between deciding whether an app should be installed on the watch at all, whether you want to use the glances and complications it provides, and custom per-app notification settings, there are so many switches you have to fiddle with that it feels like serious work. I wish this were simpler. I can’t think of a better way to handle the complexity, though.

# Conclusion

We are used to Apple’s 1.0 products being feature-constrained where the existing features are very well executed. The watch is different. There’s an argument to be made that the UI is too complicated and overloaded, and that Apple should have launched the watch without third-party apps. I’m not sure how much that would have changed the public perception, though. Apple’s own apps are often too slow to be useful (try starting a navigation in Maps), too, so we’re either talking about a much more simplified watch without apps at all or a launch of a much faster model at a later time, perhaps in late 2016 or early 2017. Given the competitive landscape and the public pressure on Apple to deliver new products, I’m not sure “the market” would have welcomed either alternative.

The one thing that’s holding the watch back the most at the moment is speed. I’m not sure the next version will make a huge performance leap (remember, the iPhone 3G wasn’t faster than the original iPhone), but performance will surely improve dramatically over time. It will be interesting to see where the watch stands on that front in two or three years.

I think it’s safe to say that I wouldn’t wear my Apple Watch anymore if it weren’t for the activity tracking. But that feature alone has hooked me to an extent that I will probably buy the next model. I may be better off with a cheaper fitness tracker, but now that I’m kind of locked into Apple’s fitness metrics I’ll probably stick with it.

Lastly, Joe Cieplinski wrote down his thoughts on the Apple Watch in an excellent three-part series that I highly recommend: [Apple Watch: Almost a Year](http://www.joecieplinski.com/blog/2016/04/26/apple-watch-almost-a-year/), [More on Apple Watch and its Appeal](http://www.joecieplinski.com/blog/2016/04/27/more-on-apple-watch-and-its-appeal/), and [Apple Watch and the Future](http://www.joecieplinski.com/blog/2016/04/28/apple-watch-and-the-future/).

1. The watch will give you weekly recommendations for this value based on last week’s performance. [↩︎](#fnref:1)
2. I noticed that the heart rate measurements are sometimes inaccurate for me, however. During a strenuous workout the watch sometimes shows values between 70 and 80 when I know my heart rate must be at least 130 to 140. The fact that these wrong measurements always seem to fall into the same range (e.g. I never see a value of 100 at such a time) makes me think the heart rate sensor sees exactly every second of my heartbeats, but that’s just speculation. [↩︎](#fnref:2)
3. David Smith recognized this, too. His app [Activity++](https://david-smith.org/apps/) (recommended) has a setting where one rest day per week doesn’t break a streak. [↩︎](#fnref:3)
4. Seriously, consumer brands, what is wrong with you? If I am stupid enough to pay €200 for a pair of your sneakers, the last thing I want is to showcase my susceptibility to your advertising by showing off your giant logos! [↩︎](#fnref:4)
