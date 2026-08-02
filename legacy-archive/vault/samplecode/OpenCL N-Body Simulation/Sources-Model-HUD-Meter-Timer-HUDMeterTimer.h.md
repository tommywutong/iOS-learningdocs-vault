---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_HUD_Meter_Timer_HUDMeterTimer_h.html
archived_at: '2026-07-18T03:17:37.937565Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-HUD-Meter-Timer-HUDMeterTimer.mm.md)[Previous](Sources-Model-HUD-Button-HUDButton.h.md)

# Sources/Model/HUD/Meter/Timer/HUDMeterTimer.h

```objc
/*
 <codex>
 <abstract>
 Utility class for manging a high-resolution timer for a hud meter.
 </abstract>
 </codex>
 */

#ifndef _HUD_METER_TIMER_H_
#define _HUD_METER_TIMER_H_

#import <valarray>

#import <OpenGL/OpenGL.h>

#ifdef __cplusplus

namespace HUD
{
    namespace Meter
    {
        typedef std::valarray<GLdouble> Vector;

        typedef uint64_t  Time;
        typedef GLdouble  Duration;

        namespace TimeScale
        {
            extern GLdouble kSeconds;
            extern GLdouble kMilliSeconds;
            extern GLdouble kMicroSeconds;
            extern GLdouble kNanoSeconds;
        };

        class Timer
        {
        public:
            Timer(const size_t& size = 20,
                  const bool& doAscend = true,
                  const GLdouble& scale = TimeScale::kSeconds);

            Timer(const Timer& timer);

            virtual ~Timer();

            Timer& operator=(const Timer& timer);

            void erase();

            bool resize(const size_t& size);

            void update(const GLdouble& dx = 1.0f);

            const GLdouble persecond() const;

            void start();
            void stop();
            void reset();

            void setScale(const GLdouble& scale);

            void setStart(const Time& time);
            void setStop(const Time& time);

            const Time& getStart() const;
            const Time& getStop()  const;

            const Duration& getDuration() const;

        private:
            bool      mbAscend;
            size_t    mnSize;
            size_t    mnCount;
            size_t    mnIndex;
            GLdouble  mnAspect;
            GLdouble  mnRes;
            GLdouble  mnScale;
            Time      mnStart;
            Time      mnStop;
            Duration  mnDuration;
            Vector    m_Vector;
        }; // Array
    } // Meter
} // HUD

#endif

#endif
```

[Next](Sources-Model-HUD-Meter-Timer-HUDMeterTimer.mm.md)[Previous](Sources-Model-HUD-Button-HUDButton.h.md)

