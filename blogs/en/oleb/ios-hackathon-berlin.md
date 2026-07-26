---
title: iOS Hackathon Berlin
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/01/ios-hackathon-berlin/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:089a23d1a3bcdeb6'
translated: false
---

> 原文：[iOS Hackathon Berlin](https://oleb.net/blog/2011/01/ios-hackathon-berlin/)　·　Ole Begemann

# iOS Hackathon Berlin

I took part in an iOS hackathon in Berlin last weekend and I had so much fun at the event that I want to tell you about it. Organized by [Appbackr](http://www.appbackr.com/) and hosted by [SoundCloud](https://soundcloud.com/), iOS developers and designers were invited to pitch ideas, form teams and build a working app in little more than a day.

The hackathon (I’ll keep calling the event “hackathon” as I can’t bring myself to use the (IMO) dreadful offical name, “Appbackrthon”) started on Friday night with a get-together of some 25 people, both coders and designers. Everybody could pitch an idea around which teams of 4-6 people formed. Kick-off for the teams was at about 10 pm, and all teams spent the rest of the Friday working on their idea and agreeing on a concept for the actual app. As team members discussed their design, some ideas underwent considerable change from the initial pitch in this phase.

After a short night, the teams met again on Saturday morning and dove deep into coding and design work. Since we would only have a few more coding hours left on Sunday before the final apps had to be presented, Saturday was the day when almost all of the implementation had to happen, from modelling the app’s structure to designing and implementing the UI. Overall, we worked for some 15 hours on Saturday and another 4 or so on Sunday.

On Sunday afternoon, each team gave a short presentation of their app; a jury then determined the winners. Here is a rundown of each team’s results in the order ranked:

# Winners: LineTime

[![LineTime screenshot on iPad](https://oleb.net/media/linetime-screenshot-ipad.png)](https://oleb.net/media/linetime-screenshot-ipad.png)

LineTime is an iPhone and iPad app that lets you interact very smoothly with a timeline of world events. The app retrieves dates and info about historical events from Wikipedia and displays them in a very cool horizontal timeline UI. Users can pan the timeline left and right to go back and forth in history, and pinch to zoom in and out in order to get a more detailed look at a certain period of time (zooming by pinching was implemented in the UI but, understandably given the limited development time, the team had not yet gotten to retrieving more info from the datasource as the user zoomed in further).

Congratulations to the LineTime team who I think totally deserved to win! Their app combines a great UI and execution with an idea that is quite unique on the App Store. And if historical data is not your thing, the timeline approach can be used to visualize any data that has a time component, from your personal calendar to your music library. The team is enthusiastic about going forward and further polishing app to make it ready for a great App Store release. Check back at [linetimeapp.com](http://linetimeapp.com/) for their progress.

[Watch the LineTime demo](http://blip.tv/file/4627680).

**Update April 5, 2011:** LineTime for the iPad is now [available on the App Store](http://itunes.apple.com/us/app/linetime/id428475853). Congratulations to the team!

# Second place: Carl the Tamagotchi for non-smokers

[![Carl screenshot on an iPhone](https://oleb.net/media/carl-screenshot-iphone.png)](https://oleb.net/media/carl-screenshot-iphone.png)

Are you a non-smoker? Do you envy the smokers at work for the regular five-minute breaks they seem to have? Are you always the last to learn about the latest gossip at the office? Then Carl is for you. Just define in the preferences what kind of smoker (light, heavy, chain) Carl is and he will nag you so hard when it is time for the next cigarette break you won’t be able to ignore him. That way, you can get the same breaks as the smokers without the negative health effects because Carl smokes your virtual cigarette for you. Carl’s path from being a totally relaxed chicken (right after a smoking break) via becoming more and more nervous (is it time yet?) to intolerable angry bird™ (when you don’t give him a break on time) is illustrated with some very cool artwork, animations, and sound effects. Kudos to the design team for pulling this off in such a short time.

Carl is perhaps the app that was best suited for the hackathon format. While it is probably not the most complex app (as if that mattered on the App Store), it is the only one of all the apps we built over the weekend that actually got really close to being finished (in the “we could totally publish this on the App Store tomorrow” sense). So I think there is a good chance we will see Carl on the App Store very soon.

[Watch the Carl demo](http://tiburontv.blip.tv/file/4621684/).

**Update March 21, 2011:** Carl is now [available on the App Store](http://itunes.apple.com/de/app/carl-das-nichtraucherkuken/id415319629?mt=8). Congratulations to the team!

# Third place: CrowdVideo

[![CrowdVideo screenshot on iPhone](https://oleb.net/media/crowdvideo-screenshot-iphone.png)](https://oleb.net/media/crowdvideo-screenshot-iphone.png)

What if your iPhone, while you recorded a video, would also continuously log your current location and the direction you are holding your iPhone in? As you move around or turn, your video would get a unique “trail” that you can later follow along with on a map when replaying the video. Now imagine you’re at a concert or sports event where hundreds of people recorded such geocoded video and uploaded it to a website. You could then re-experience the event from many different angles. In essence, you would be your own director. This is exactly what the CrowdVideo team built, and I think it’s an awesome idea.

Unfortunately, such a thing is not only difficult to build in one day, it is also hard to demo when you don’t really have time to prepare good video material. So the demo of the CrowdVideo app fell a little short and these guys still have a lot of work to do before their app is ready for publication, but I think this might be the idea with the most potential.

[Watch the CrowdVideo demo](http://blip.tv/file/4627569).

# Proud forth place: Fridge Notes

[![Fridge Notes screenshot on iPad](https://oleb.net/media/fridgenotes-screenshot-ipad.png)](https://oleb.net/media/fridgenotes-screenshot-ipad.png)

This was my team. Our idea was to build yet another note-taking/to-do app, this time with a focus on real-world design and family collaboration. We chose the family fridge as the metaphor where people would post sticky notes for themselves or other family members to see. The entire family would then be able to check what’s on the fridge from their iPads, iPhones, or iPod touches (though we did not have time to build the server component or an iPhone client on the weekend; it’s iPad-only at the moment).

The app is supposed to be graphically very attractive, with lots of animations and a “real-world” feel to it. It is certainly not perfect yet but I think we were able to give it a nice touch. Despite “only” reaching fourth place, I am quite proud of what we have achieved over the weekend. Taking into account that we team members did not know each other very well (or at all) and never worked together before, dividing up the coding tasks and pushing to a shared Git repository worked remarkably well. We also faced some interesting programming challenges regarding gesture recognition and animation, so I certainly learned a lot. If the jury prioritized the originality of the idea and the market chances in their assessment (and rightly so), they were certainly right to rank us fourth.

One more personal lesson learned: I spent all four coding hours on Sunday on a nice-but-not-necessary feature that we ended up not including in the demo app because I couldn’t fix one last bug that could have ruined the demo. If you’re on a tight and fixed schedule, your time is probably better spent polishing existing features than trying to add new ones.

[Watch the FridgeNotes demo](http://tiburontv.blip.tv/file/4621620/).

# More videos and photos

- [More videos, shot by Viktoria Trosien for tiburon-tv.com](http://tiburontv.blip.tv/search?q=appbackrthon)
- [Photos from the hackathon on Facebook](https://www.facebook.com/album.php?aid=301228&amp;id=313009587257)
- [More photos by Leon Weidauer](http://galleries.techpriester.net/appbackrthon/)

# Conclusion

I hope this was not the last event of its kind in Berlin. If you ever have the chance to join a hackathon, I highly recommend it. Thanks again to the organizers and sponsors: [Appbackr](http://www.appbackr.com/), [SoundCloud](https://soundcloud.com/), [Blackbox](http://blackbox.vc/), [Madvertise](http://www.madvertise.de/), and [Trademob](http://www.trademob.com/).
