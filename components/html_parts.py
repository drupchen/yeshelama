from textwrap import dedent

head = dedent("""\
<!-- Last updated for Version 2.1 -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>བཀའ་ཁྲིད་ཐོས་ཀློག་སྦྲགས་མ།</title>
    <link rel="stylesheet" href="../css/hyperaudio-lite-player.css">
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jomolhari">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.5.0/velocity.js"></script>
    <style>
      :root {
        --primary-color: #4f6fa7; /* Softer blue */
        --secondary-color: #475569;
        --accent-color: #d48b4e; /* Soft amber/gold */
        --background-color: #f7fafc;
        --text-color: #23272f;
        --light-gray: #f5f6fa;
        --border-color: #e2e8f0;
        --hover-color: #e3e7ee;
        --timecode-bg: #f9f5e7;
        --timecode-text: #d48b4e;
        --active-bg: #f7f3e7;
        --active-highlight: #d4a94e;
        --card-shadow: 0 4px 16px rgba(79, 111, 167, 0.07), 0 1.5px 4px rgba(0, 0, 0, 0.06);
      }

      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }

      body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        line-height: 1.7;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 0;
        margin: 0;
        min-height: 100vh;
        font-size: 1.07rem;
        letter-spacing: 0.01em;
      }

      .container {
        width: 100%;
        max-width: 1024px;
        margin: 0 auto;
        padding: 2rem 1rem;
      }

      @media (max-width: 768px) {
        .container {
          padding: 1.5rem 1rem;
        }
      }

      header {
        margin-bottom: 3rem;
        text-align: center;
        padding: 1.5rem 0;
      }

      h1 {
        font-size: 2.7rem;
        font-weight: 800;
        margin-bottom: 1.1rem;
        color: var(--secondary-color);
        letter-spacing: -0.025em;
        text-shadow: 0 2px 8px rgba(79, 111, 167, 0.05);
      }

      h2 {
        font-size: 2rem;
        font-weight: 700;
        margin: 2.5rem 0 1.2rem;
        color: var(--secondary-color);
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 0.6rem;
        letter-spacing: -0.012em;
      }

      h3 {
        font-size: 1.35rem;
        font-weight: 500;
        margin: 1.75rem 0 0.75rem;
        color: var(--secondary-color);
        letter-spacing: -0.01em;
      }

      audio {
        width: 100%;
        margin: 1rem 0 0;
        border-radius: 21px;
        box-shadow: var(--card-shadow);
        height: 40px;
        transition: all 0.3s ease;
      }

      audio:focus,
      audio:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.05), 0 3px 6px rgba(0, 0, 0, 0.08);
        transform: translateY(-1px);
      }

      /* Audio player styling */

      /* Session links styling */
      /* Table of contents styling */

      .toc-section {
        background-color: #fff;
        border-radius: 18px;
        padding: 1.5rem 1.25rem;
        margin: 2rem 0;
        box-shadow: var(--card-shadow);
        border: 1.5px solid var(--border-color);
        transition: box-shadow 0.2s, border-color 0.2s;
      }

      .toc-section:last-child {
        margin-bottom: 0;
      }

      .toc-section-title {
        font-size: 1.22rem;
        font-weight: 700;
        color: var(--secondary-color);
        margin-bottom: 1.3rem;
        padding-bottom: 0.35rem;
        border-bottom: 1.5px solid var(--border-color);
        letter-spacing: 0.01em;
      }
      .toc-section-title .tibetan {
        font-size: 1.5em;
        line-height: 1.3em;
      }

      .toc-section-subtitle {
        font-size: 0.9rem;
        opacity: 0.6;
      }

      /* Session links styling */
      .session-links {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 0.35rem;
        padding: 1rem 0;
        border-bottom: 1px solid var(--light-gray);
      }
      .session-links:first-child {
        padding-top: 0;
      }
      .session-links:last-child {
        border-bottom: 0;
        padding-bottom: 0;
      }

      /* Section dividers */
      .section-divider {
        margin: 8rem 0;
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, transparent, var(--border-color), transparent);
      }

      .session-links a {
        text-decoration: none;
        color: var(--primary-color);
        font-size: 0.8rem;
        font-weight: 600;
        padding: 0.3rem 0.7rem 0.3rem 1rem;
        border-radius: 9999px;
        background-color: var(--light-gray);
        transition: all 0.18s;
        display: inline-flex;
        align-items: center;
        box-shadow: 0 1.5px 5px rgba(79, 111, 167, 0.08);
        width: fit-content;
        gap: 0.7rem;
      }

      .session-links a:hover {
        background-color: var(--hover-color);
        box-shadow: 0 4px 12px rgba(212, 169, 78, 0.11);
      }

      .timecode {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background-color: var(--timecode-bg);
        color: var(--timecode-text);
        font-size: 0.875rem;
        font-weight: 500;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        margin-left: 0.5rem;
        font-family: 'Inter', sans-serif;
        letter-spacing: 0.02em;
      }
      
      .session {
        font-size: 0.875rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
      }
      
      .session-links .tibetan {
        font-size: 15pt;
        color: #1d458c;
        display: block;
        text-align: center;
        margin-bottom: 0.1em;
        white-space: nowrap;
      }
      .session-links .english {
        font-family: 'Inter', sans-serif;
        display: block;
        text-align: center;
        margin-bottom: 0.05em;
      }

      .session-links .human-time {
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--accent-color);
        background-color: var(--timecode-bg);
        padding: 0.22rem 0.7rem;
        border-radius: 9999px;
        min-width: 3.3rem;
        text-align: center;
        display: inline-block;
        letter-spacing: 0.01em;
        box-shadow: 0 1.5px 4px rgba(212, 169, 78, 0.07);
      }

      .tibetan {
        font-family: Jomolhari, serif;
        font-weight: normal;
      }

      h2 {
        margin-top: 2em;
      }

      h2 span.tibetan {
        font-size: 1em;
        display: block;
        line-height: 1.3em;
      }

      /* Improve spacing for timecodes in transcript */
      .hyperaudio-transcript .timecode {
        position: relative;
        top: 10px;
        display: inline-flex;
        justify-content: center;
        min-width: 3.5rem;
        margin: 0 5px;
        padding: 0 !important;
        vertical-align: top;
      }

      /* Transcript styling */
      .hyperaudio-transcript {
        resize: vertical;
        overflow-y: auto;
        max-height: 500px;
        width: 100%;
        scrollbar-gutter: stable;
        position: relative;
        border: 1.5px solid var(--border-color);
        border-radius: 6px;
        padding: 2.1rem 1.2rem;
        background-color: #fff;
        margin: 1.3rem 0 2.7rem;
        font-family: Jomolhari, serif;
        font-size: 1.6rem;
        line-height: 1.85;
        box-shadow: var(--card-shadow);
        transition: box-shadow 0.3s, border-color 0.2s;
      }

      .hyperaudio-transcript a {
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s;
      }
      .hyperaudio-transcript a:hover {
        background: var(--hover-color);
        border-color: var(--primary-color);
      }
      .hyperaudio-transcript a.active {
        background-color: #d9f3fc !important;
        border-color: #d9f3fc !important;
      }

      /* Custom scrollbar for modern look */
      .hyperaudio-transcript::-webkit-scrollbar {
        width: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-track {
        background: var(--light-gray);
        border-radius: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-thumb {
        background-color: var(--border-color);
        border-radius: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-thumb:hover {
        background-color: var(--secondary-color);
      }

      .hyperaudio-transcript p > .active {
        background-color: rgba(59, 130, 246, 0.2);
        text-decoration: var(--active-highlight) underline;
        text-decoration-thickness: 2px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
      }

      .hyperaudio-transcript p > .unread:not(.active) {
        opacity: 0.7;
      }

      #clipboard-text {
        font-family: Jomolhari, monospace;
        padding: 0.75rem;
        background-color: var(--light-gray);
        border-radius: 4px;
        margin: 0.5rem 0;
      }

      #clipboard-confirm {
        font-size: 0.875rem;
        color: var(--accent-color);
        margin-top: 0.5rem;
      }

      /* Tibetan text styling - preserving original fonts */
      [lang='bo'] {
        font-family: Jomolhari, serif;
      }
    </style>

  </head>""")

body_beginning = dedent("""\
    <body>
      <div id="popover"><a id="popover-btn">Copy to clipboard<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="-130 -110 600 600"><path d="m161,152.9h190c0.1,0 0.1,0 0.2,0 10.8,0 19.6-7.1 19.6-16 0-1.5-14.1-82.7-14.1-82.7-1.3-7.9-9.6-13.8-19.4-13.8l-61.7,.1v-13.5c0-8.8-8.8-16-19.6-16-10.8,0-19.6,7.1-19.6,16v13.6l-61.8,.1c-9.8,0-18,5.9-19.4,13.8l-13.7,80.3c-1.2,14.3 13.5,18.1 19.5,18.1z" fill="currentcolor"/><path d="m427.5,78.9h-26.8c0,0 9.3,53.5 9.3,58 0,30.4-26.4,55.2-58.8,55.2h-190.2c-19.6,0.4-63.3-14.7-58.1-63.9l8.4-49.2h-26.8c-10.8,0-19.6,8.8-19.6,19.6v382.9c0,10.8 8.8,19.6 19.6,19.6h343c10.8,0 19.6-8.8 19.6-19.6v-383c0-10.8-8.8-19.6-19.6-19.6zm-76.5,320.1h-190c-10.8,0-19.6-8.8-19.6-19.6 0-10.8 8.8-19.6 19.6-19.6h190c10.8,0 19.6,8.8 19.6,19.6 0,10.8-8.7,19.6-19.6,19.6zm0-110.3h-190c-10.8,0-19.6-8.8-19.6-19.6 0-10.8 8.8-19.6 19.6-19.6h190c10.8,0 19.6,8.8 19.6,19.6 0,10.8-8.7,19.6-19.6,19.6z" fill="currentcolor"/></svg></a></div>

<dialog id="clipboard-dialog">
    <h3>The following text has been copied to the clipboard</h3>
    <p id=clipboard-text></p>
    <div style="text-align: right;">
      <button id="clipboard-confirm">ok</button>
    </div>
</dialog>
          """)

player_start = '<audio id="hyperplayer1" style="position:relative; width:97%" src="'

audio_links = {
    "A1": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406737079-44100-2-1248d6de476e6.m4a",
    "A2": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/14eb2917-f211-7e78-1a20-2e8f24c945de.mp3",
    "A3": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/6b385cbf-9f65-f8b8-cf07-164c3397fbc1.mp3",
    "A4": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406737231-44100-2-e64026282b7e8.m4a",
    "A5": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406737277-44100-2-9c9dc845aee6b.m4a",
    "A6": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/6d7def0d-448e-565e-d538-d541fbb7d3f7.mp3",
    "A7": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406737428-44100-2-b6925d7b86df7.m4a",
    "A8": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406737493-44100-2-d2a9ec7c1d7fd.m4a",
    "A9": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/020bbf50-f973-4857-d83c-3a723a5bad15.mp3",
    "A10": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406737614-44100-2-ce17331536d66.m4a",
    "A11": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/f8544989-df9f-508b-10ea-a0b2ebecd317.mp3",
    "A12": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406737750-44100-2-a0655fe7bc83f.m4a",
    "A13": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406737800-44100-2-7ed22a8137a69.m4a",
    "A14": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406737884-44100-2-7a1c1199ce4bb.m4a",
    "A15": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/db2d3fbc-0503-fcd9-e727-b7600bd48524.mp3",
    "A16": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/76891969-42c7-22a3-50c4-0c98241d9ad5.mp3",
    "A17": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406738076-44100-2-a01133620d958.m4a",
    "A18": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406dc490-e031-6107-e429-aaa1b3834b65.mp3",
    "A19": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/43be0c99-94f9-b5d1-248e-d8faef0e8f87.mp3",
    "A20": 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407428468-44100-2-e4fe99b6ceb97.m4a',
    'A21': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407428515-44100-2-39429612e144a.m4a',
    'A22': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/673a77cc-53eb-1bc3-af0b-ab6d1a91e4a7.mp3',
    'A23': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/1e7b0499-f05d-1026-80fd-19aea6fd92d7.mp3',
    'A24': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407428642-44100-2-c8c66bf4e29ec.m4a',
    'B1': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/b843dc81-4e09-f743-44f3-b33881a10f0b.mp3',
    'B2': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/a0eaae15-7ed6-ff2f-dcbe-7522e6dabd19.mp3',
    'B3': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/8c59f6ea-86f7-c2b5-8401-8b32317f55e7.mp3',
    'B4': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407428745-44100-2-45ea69f10fd58.m4a',
    'B5': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407428998-44100-2-fe8247188af58.m4a',
    'B6': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407429017-44100-2-a0e44e5d01252.m4a',
    'B7': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407429036-44100-2-37eef801e29a3.m4a',
    'B8': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/6ed59dc2-fe51-f93c-7fec-67f327771986.mp3',
    'B9': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/459af35f-726b-fe09-0966-51db207b616b.mp3',
    'B10': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/62cd23cd-c566-7566-3f75-572f51a81743.mp3',
    'B11': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/e36063a4-325c-eb84-285a-d5070456cd88.mp3',
    'B12': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407429176-44100-2-51806a5ef249a.m4a',
    'B13': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/73700c91-3f93-162c-ab9f-193fdfec09c7.mp3',
    'B14': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/384299f3-c1a4-f364-c8a8-6b326e6fb996.mp3',
    'B15': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/b02dab35-56b1-c72f-ef8b-ec0d3fba8dd8.mp3',
    'B16': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/c2bed140-ff25-a298-c874-b3b2b9def988.mp3',
    'B17': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/444805ac-07f7-767f-25fe-aa9b5d80e383.mp3',
    'B18': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/9b02bb40-9c03-3b94-0870-b1bf5fcf0f76.mp3',
    'B19': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407432271-44100-2-70ac78dfa4f47.m4a',
    'B20': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/abd779a9-130d-cd67-ee1c-ecfab21e8282.mp3',
    'B21': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/2546b8f8-89fe-e5e3-02ee-6cd2f71febc3.mp3',
    'B22': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/a4048fef-b18e-479d-853e-56135b6154cd.mp3',
    'B23': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/b48fffd7-7fe1-253a-5a40-70cfece0461b.mp3',
    'B24': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407432433-44100-2-0b069c65a92d9.m4a',
    'B25': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/6b4929c7-05fb-4e60-400c-966fdb2fe6d6.mp3',
    'B26': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/20489d0d-6bdb-a6a7-d6bf-193a1826b662.mp3',
    "C1": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406736739-44100-2-c97d74f8a6b2a.m4a",
    'C2': "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406736570-44100-2-27f390b28e1d1.m4a",
    "C3": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406736665-44100-2-2527d398de1d9.m4a",
    "C4": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406736793-44100-2-f64624c211131.m4a",
    'C5': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407432530-44100-2-57443b90e8fa2.m4a',
    'C6': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-13/407432560-44100-2-a1f7919d7a4c5.m4a',
    "C7": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406736834-44100-2-6882ddcdb934f.m4a",
    "C8": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406736888-44100-2-e71622ff2b752.m4a",
}
player_middle = '" type="audio/'
player_end = '" controlsList="nodownload" controls></audio>'

transcript_start = """\
          
          <div id="hypertranscript1" class="hyperaudio-transcript" style="resize: vertical; overflow-y:scroll; height:800px; width: 97%; scrollbar-gutter: stable; position:relative; border-style:dashed; border-width: 1px; border-color:#999; padding: 8px">
          <article><section>"""

transcript_end = dedent("""\
          </section></article>
          </div>""")

body_end = dedent("""\
      <script src="https://w.soundcloud.com/player/api.js"></script>
      <script src="../js/hyperaudio-lite.js"></script>
      <script src="../js/hyperaudio-lite-extension.js"></script>
      <script>
      // minimizedMode is still experimental - it aims to show the current words in the title, which can be seen on the browser tab.
      let minimizedMode = false;
      let autoScroll = true;
      let doubleClick = false;
      let webMonetization = false;

      new HyperaudioLite("hypertranscript1", "hyperplayer1", minimizedMode, autoScroll, doubleClick, webMonetization);
      </script>
      <script>
        var coll = document.getElementsByClassName("collapsible");
        var i;

        for (i = 0; i < coll.length; i++) {
          coll[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.display === "block") {
              content.style.display = "none";
            } else {
              content.style.display = "block";
            }
          });
        }
      </script>
  </body>
</html>""")

index_head = dedent("""\
<!-- Last updated for Version 2.1 -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ཡེ་ཤེས་བླ་མ།</title>
    <link rel="stylesheet" href="css/hyperaudio-lite-player.css" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jomolhari" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.5.0/velocity.js"></script>
    <style>
      :root {
        --primary-color: #4f6fa7; /* Softer blue */
        --secondary-color: #475569;
        --accent-color: #d48b4e; /* Soft amber/gold */
        --background-color: #f7fafc;
        --text-color: #23272f;
        --light-gray: #f5f6fa;
        --border-color: #e2e8f0;
        --hover-color: #e3e7ee;
        --timecode-bg: #f9f5e7;
        --timecode-text: #d48b4e;
        --active-bg: #f7f3e7;
        --active-highlight: #d4a94e;
        --card-shadow: 0 4px 16px rgba(79, 111, 167, 0.07), 0 1.5px 4px rgba(0, 0, 0, 0.06);
      }

      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }

      body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        line-height: 1.7;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 0;
        margin: 0;
        min-height: 100vh;
        font-size: 1.07rem;
        letter-spacing: 0.01em;
      }

      .container {
        width: 100%;
        max-width: 1024px;
        margin: 0 auto;
        padding: 2rem 1rem;
      }

      @media (max-width: 768px) {
        .container {
          padding: 1.5rem 1rem;
        }
      }

      header {
        margin-bottom: 3rem;
        text-align: center;
        padding: 1.5rem 0;
      }

      h1 {
        font-size: 2.7rem;
        font-weight: 800;
        margin-bottom: 1.1rem;
        color: var(--secondary-color);
        letter-spacing: -0.025em;
        text-shadow: 0 2px 8px rgba(79, 111, 167, 0.05);
      }

      h2 {
        font-size: 2rem;
        font-weight: 700;
        margin: 2.5rem 0 1.2rem;
        color: var(--secondary-color);
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 0.6rem;
        letter-spacing: -0.012em;
      }

      h3 {
        font-size: 1.35rem;
        font-weight: 500;
        margin: 1.75rem 0 0.75rem;
        color: var(--secondary-color);
        letter-spacing: -0.01em;
      }

      audio {
        width: 100%;
        margin: 1rem 0 0;
        border-radius: 21px;
        box-shadow: var(--card-shadow);
        height: 40px;
        transition: all 0.3s ease;
      }

      audio:focus,
      audio:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.05), 0 3px 6px rgba(0, 0, 0, 0.08);
        transform: translateY(-1px);
      }

      /* Audio player styling */

      /* Session links styling */
      /* Table of contents styling */

      .toc-section {
        background-color: #fff;
        border-radius: 18px;
        padding: 1.5rem 1.25rem;
        margin: 2rem 0;
        box-shadow: var(--card-shadow);
        border: 1.5px solid var(--border-color);
        transition: box-shadow 0.2s, border-color 0.2s;
      }

      .toc-section:last-child {
        margin-bottom: 0;
      }

      .toc-section-title {
        font-size: 1.22rem;
        font-weight: 700;
        color: var(--secondary-color);
        margin-bottom: 1.3rem;
        padding-bottom: 0.35rem;
        border-bottom: 1.5px solid var(--border-color);
        letter-spacing: 0.01em;
      }
      .toc-section-title .tibetan {
        font-size: 1.5em;
        line-height: 1.3em;
      }

      .toc-section-subtitle {
        font-size: 0.9rem;
        opacity: 0.6;
      }

      /* Session links styling */
      .session-links {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 0.35rem;
        padding: 1rem 0;
        border-bottom: 1px solid var(--light-gray);
      }
      .session-links:first-child {
        padding-top: 0;
      }
      .session-links:last-child {
        border-bottom: 0;
        padding-bottom: 0;
      }

      /* Section dividers */
      .section-divider {
        margin: 8rem 0;
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, transparent, var(--border-color), transparent);
      }

      .session-links a {
        text-decoration: none;
        color: var(--primary-color);
        font-size: 0.8rem;
        font-weight: 600;
        padding: 0.3rem 0.7rem 0.3rem 1rem;
        border-radius: 9999px;
        background-color: var(--light-gray);
        transition: all 0.18s;
        display: inline-flex;
        align-items: center;
        box-shadow: 0 1.5px 5px rgba(79, 111, 167, 0.08);
        width: fit-content;
        gap: 0.7rem;
      }

      .session-links a:hover {
        background-color: var(--hover-color);
        box-shadow: 0 4px 12px rgba(212, 169, 78, 0.11);
      }

      .timecode {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background-color: var(--timecode-bg);
        color: var(--timecode-text);
        font-size: 0.875rem;
        font-weight: 500;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        margin-left: 0.5rem;
        font-family: 'Inter', sans-serif;
        letter-spacing: 0.02em;
      }
      
      .session {
        font-size: 0.875rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
      }
      
      .session-links .tibetan {
        font-size: 15pt;
        color: #1d458c;
        display: block;
        text-align: center;
        margin-bottom: 0.1em;
        white-space: nowrap;
      }
      .session-links .english {
        font-family: 'Inter', sans-serif;
        display: block;
        text-align: center;
        margin-bottom: 0.05em;
      }

      .session-links .human-time {
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--accent-color);
        background-color: var(--timecode-bg);
        padding: 0.22rem 0.7rem;
        border-radius: 9999px;
        min-width: 3.3rem;
        text-align: center;
        display: inline-block;
        letter-spacing: 0.01em;
        box-shadow: 0 1.5px 4px rgba(212, 169, 78, 0.07);
      }

      .tibetan {
        font-family: Jomolhari, serif;
        font-weight: normal;
      }

      h2 {
        margin-top: 2em;
      }

      h2 span.tibetan {
        font-size: 1em;
        display: block;
        line-height: 1.3em;
      }

      /* Improve spacing for timecodes in transcript */
      .hyperaudio-transcript .timecode {
        position: relative;
        top: 10px;
        display: inline-flex;
        justify-content: center;
        min-width: 3.5rem;
        margin: 0 5px;
        padding: 0 !important;
        vertical-align: top;
      }

      /* Transcript styling */
      .hyperaudio-transcript {
        resize: vertical;
        overflow-y: auto;
        max-height: 500px;
        width: 100%;
        scrollbar-gutter: stable;
        position: relative;
        border: 1.5px solid var(--border-color);
        border-radius: 6px;
        padding: 2.1rem 1.2rem;
        background-color: #fff;
        margin: 1.3rem 0 2.7rem;
        font-family: Jomolhari, serif;
        font-size: 1.6rem;
        line-height: 1.85;
        box-shadow: var(--card-shadow);
        transition: box-shadow 0.3s, border-color 0.2s;
      }

      .hyperaudio-transcript a {
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s;
      }
      .hyperaudio-transcript a:hover {
        background: var(--hover-color);
        border-color: var(--primary-color);
      }
      .hyperaudio-transcript a.active {
        background-color: #d9f3fc !important;
        border-color: #d9f3fc !important;
      }

      /* Custom scrollbar for modern look */
      .hyperaudio-transcript::-webkit-scrollbar {
        width: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-track {
        background: var(--light-gray);
        border-radius: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-thumb {
        background-color: var(--border-color);
        border-radius: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-thumb:hover {
        background-color: var(--secondary-color);
      }

      .hyperaudio-transcript p > .active {
        background-color: rgba(59, 130, 246, 0.2);
        text-decoration: var(--active-highlight) underline;
        text-decoration-thickness: 2px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
      }

      .hyperaudio-transcript p > .unread:not(.active) {
        opacity: 0.7;
      }

      #clipboard-text {
        font-family: Jomolhari, monospace;
        padding: 0.75rem;
        background-color: var(--light-gray);
        border-radius: 4px;
        margin: 0.5rem 0;
      }

      #clipboard-confirm {
        font-size: 0.875rem;
        color: var(--accent-color);
        margin-top: 0.5rem;
      }

      /* Tibetan text styling - preserving original fonts */
      [lang='bo'] {
        font-family: Jomolhari, serif;
      }
    </style>
  </head>""")

index_body = dedent("""\
  <body>
    <div class="toc-section">""")

index_link_start = '\n<a href="sessions/transcript_'
index_link_start2 = '.html#hypertranscript1='
index_link_middle1a = '"><span class="session-a"><span class="session">'
index_link_middle1b = '"><span class="session-b"><span class="session">'
index_link_middle1c = '"><span class="session-c"><span class="session">'
index_link_middle2 = ' </span><span class="tibetan">'
index_link_end = '</span></span></a>'

index_end = dedent("""\
    </div>
  </body>
</html>
""")