---
title: Manim
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/manim/'
original_language: en
published: 2025-10-01
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:381ba60ce76ada8c'
translated: false
---

> 原文：[Manim](https://nshipster.com/manim/)　·　NSHipster (Mattt)

# [Manim](https://nshipster.com/manim/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  October 1^st, 2025

A few years ago, Twitter user [@38mo1](https://x.com/38mo1/), a chemistry teacher from Japan, posted a [Halloween × Boolean logic meme](https://x.com/38mo1/status/1320004943542009857) that I liked enough to save to `~/Downloads`. And ever since, I’ve had a yearly reminder every October 1st to open the image and get a seasonal chuckle 🎃

More recently, I wanted to teach my kids some advanced snake maths ([long story](https://www.youtube.com/watch?v=ysaIAwxl7fc) 🐍) and remembered that the software [3blue1brown](https://www.youtube.com/c/3blue1brown) uses for their videos was open-source.

Which is all to say that this year for Halloween, NSHipster is dressing up as a beloved YouTuber. How’d I do?

_Neat, right?_ Everything used to create that video [available on GitHub](https://github.com/nshipster/trick-xor-treat). Read on to learn more about how to get started on your next great explainer.

---

Back in 2015, Grant Sanderson found himself at a hackathon with a desire to practice his Python skills. What emerged was “very scrappy code for visualizing functions as transformations” — a playful experiment that would eventually become the foundation of both the 3Blue1Brown YouTube channel (now 6.5+ million subscribers strong) and Manim itself.

## 0 to 1

Manim has a reputation for being difficult to install. Some of this is a natural consequence for a tool whose audience extends to self-described non-programmers. Some of this is intrinsic to working with motion graphics. And being written in Python doesn’t do it any favors (though `uv` pretty much solves all the complaints anyone could have).

Docker was more or less invented to solve the problem of packaging Python applications with system dependencies, so it’s entirely appropriate to wash your hands of everything and [run Manim with Docker](https://docs.manim.community/en/stable/installation/docker.html):

```
$ docker run --rm -it -v "/full/path/to/your/directory:/manim" manimcommunity/manim manim -qm scene.py MySceneName
```

…but that feels like giving up.

And besides, you’ll appreciate having a proper Python development environment once you’re up-and-running. Stick with me, and I promise everything will be A-OK (pinky swear 🤙).

### An opinionated setup guide for Manim on macOS in 2025

First, let’s do some _mise en place_:

```
# Install mise
$ brew install mise

# Install Python and uv
$ mise use -g [email protected] uv@latest
```

- [Homebrew](https://brew.sh) is a package manager for macOS. It’s the best way to install the system dependencies we need to run Manim.
- [Mise](https://mise.jdx.dev) is a polyglot tool manager. While you _could_ use Homebrew to install Python, you often need to keep a few versions around to work across different projects. So that’s what we’ll recommend here.
- [uv](https://docs.astral.sh/uv/) is a Python package manager. It’s wicked fast and _just works™_.

Now, let’s create our project and make ourselves at home:

```
# Create a new project
$ uv init my-explainer

$ cd my-explainer
# Now open with your preferred $EDITOR
```

Next, go ahead and install Manim’s system dependencies:

```
# Install Manim dependencies
$ brew install pkg-config cairo # for graphics
$ brew install --cask mactex-no-gui # for ƒοrmυℓαѕ
$ brew install sox # for voiceovers
```

- [Cairo](https://www.cairographics.org) is a 2D graphics library. You need `pkg-config` to get the Pycairo bindings working properly.
- [MacTex](https://www.tug.org/mactex/) is a LaTeX distribution for macOS. You’ll need this to make a proper maths explainer with impressive-looking formulas. We recommend downloading `mactex-no-gui`, which foregoes the GUI apps that ship in the full version.
- [SoX](https://sourceforge.net/projects/sox/) is a utility for converting audio files to different formats. Manim has some nice-_ish_ affordances for putting voice-overs into your scenes, and you’ll need SoX to take advantage of them.

Finally, let’s run a health check to see if we’re still on the happy path:

```
# Is everything working? (🫣)
$ uv run manim checkhealth
```

_Huzzah!_

## Setting the Scene

The Manim API is [rich and well-documented](https://docs.manim.community/en/stable/tutorials_guides.html), with an [extensive collection of examples](https://docs.manim.community/en/stable/examples.html). Rather than attempt to explain everything here, let’s look at one concrete example to get a sense of how it all works.

Here’s a standalone “Trick XOR Treat” scene:

```
from manim import *

class TrickXORTreat(Scene):
    def construct(self):
        # Panel background
        panel_bg = RoundedRectangle(width=7, height=5, corner_radius=0.2).set_fill(
            GREY, opacity=1
        )

        # Title
        title = Text("Trick XOR Treat").scale(0.8)
        title.move_to(panel_bg.get_top() + DOWN * 0.4)

        # Two circles for the Venn diagram
        c1 = Circle(radius=1.4, color=BLACK).move_to(LEFT * 0.8)
        c2 = Circle(radius=1.4, color=BLACK).move_to(RIGHT * 0.8)

        # Create individual fill shapes for XOR (exclusive OR)
        left_only = Difference(c1, c2).set_fill(ORANGE, opacity=0)
        right_only = Difference(c2, c1).set_fill(ORANGE, opacity=0)
        center = Intersection(c1, c2).set_fill(GREY, opacity=0)  # XOR excludes center

        # Create faces on left and right sections
        face = VGroup()
        # Left face
        left_eye = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        left_eye.move_to(left_only.get_center() + UL * 0.3)
        left_mouth = ParametricFunction(
            lambda t: [t, 0.15 * np.sin(t * PI * 5), 0], t_range=[-0.3, 0.3]
        ).set_stroke(color=BLACK, width=8)
        left_mouth.move_to(left_only.get_center() + DOWN * 0.2)
        # Right face
        right_eye = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        right_eye.move_to(right_only.get_center() + UR * 0.3)
        right_mouth = ParametricFunction(
            lambda t: [t, 0.15 * np.sin(t * PI * 5), 0], t_range=[-0.3, 0.3]
        ).set_stroke(color=BLACK, width=8)
        right_mouth.move_to(right_only.get_center() + DOWN * 0.2)
        face.add(left_eye, left_mouth, right_eye, right_mouth)

        # Combine everything
        panel = VGroup(
            panel_bg,
            left_only,
            right_only,
            center,
            VGroup(c1, c2),  # Circle outlines
            title,
            face,
        )
        panel.move_to(ORIGIN)

        # Animate the panel appearing with smooth scaling
        self.play(FadeIn(panel_bg, scale=1.1), Write(title, run_time=1.2), run_time=1.0)

        # Draw circles sequentially
        self.play(Create(c1, run_time=1.0))
        self.wait(0.5)
        self.play(Create(c2, run_time=1.0))
        self.wait(0.5)

        # Dramatic filling animations with smooth rate functions
        self.play(
            left_only.animate.set_fill(ORANGE, opacity=1),
            run_time=1.2,
            rate_func=smooth,
        )
        self.wait(0.5)

        self.play(
            right_only.animate.set_fill(ORANGE, opacity=1),
            run_time=1.2,
            rate_func=smooth,
        )
        self.wait(0.5)

        # Animate faces appearing on top of fills with bounce
        self.play(FadeIn(face, shift=UP * 0.3, scale=0.8), run_time=0.8)

        # Final pause
        self.wait(1.5)
```

The Manim API is refreshingly procedural— a nice break from the declarative nature of SwiftUI, if you ask me. You create objects, position them, and then explicitly tell them what to do. The `.animate` syntax provides some syntactic sugar for transformations, but at its core, this is imperative programming at its finest.

## Enter the Development Loop

Our example project includes a Mise task for quickly previewing our scene. It runs Manim at a low [resolution](https://www.youtube.com/watch?v=1unkluyh2Ks) (480p) and [frame rate](https://www.youtube.com/watch?v=DyqjTZHRdRs) (15 fps), and then opens the generated file in QuickTime Player.

```
$ mise run preview
```

The project also has a `render` task for when you’re ready to share it around:

```
$ mise run render
```

If everything works as intended, you should see something like this:

## (Voiceover)

No 3blue1brown explainer video would be complete without the dulcet baritone of its creator. Alas, Mr. Sanderson had previous obligations that took him away from our costume party, so we’ll have to improvise. Let’s crank up the spook factor and have an AI… _ghost? I guess?_ narrate our flick.

[ElevenLabs](https://elevenlabs.io) has some scary-good text-to-speech models. While `manim-voiceover` provides integration, it’s currently a bit temperamental with Python 3.13 and doesn’t support the latest [v3 models](https://elevenlabs.io/v3) for hyper-realistic voiceovers.

To get started, you import from `manim_voiceover` (`_fixed`) and update the scene to inherit from `VoiceoverScene`.

```
from manim_voiceover_fixed import VoiceoverScene
from manim_voiceover_fixed.services.elevenlabs import ElevenLabsService

class TrickXORTreat(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_name="Liam",
                model="eleven_v3",
                transcription_model=None,  # <-- workaround for https://github.com/ManimCommunity/manim-voiceover/issues/114
            )
        )

        with self.voiceover(
            text="""[annoyingly high-pitch nasal pedantic] Well, actually,
                    it's an exclusive or, also known as XOR..."""
        ):
            # This wait() automatically waits until the voiceover finishes!
            self.wait()
```

The `wait()` inside the context manager waits until the voiceover finishes — no manual timing required. For recorded voiceovers especially, this dramatically cuts down on how much time you spend in post getting the timing right. In fact, the finished video at the top was entirely rendered by Manim— without any touch-ups in Final Cut or Premiere!

The first time you run this code, Manim will helpfully (albeit unexpectedly) prompt you to enter an API token, which you can get [in your account dashboard](https://elevenlabs.io/app/developers). That’ll get saved to an [`.env` file](https://nshipster.com/1password-cli/) and that should be the end of it.

---

The best explainer videos don’t just teach, they spark curiosity, they delight, they make complex ideas feel approachable. That’s what drew me to 3blue1brown in the first place, and why I’ve kept that silly meme in my Downloads folder all these years.

So if you’ve been sitting on a meme in your `~/Downloads` folder, or just want an excuse to dust off those Python skills, maybe this Halloween _you_ dress up as a math YouTuber, too. The costume’s open source, and honestly? It’s a pretty good look.
