<h1 style="color: rgb(0, 0, 0); font-style: normal; font-variant:
  normal; letter-spacing: normal; line-height: normal; text-align:
  start; text-indent: 0px; text-transform: none; white-space:
  normal; word-spacing: 0px;"><font face="Helvetica, Arial,
    sans-serif">CAVEUtil</font></h1>
<font face="Helvetica, Arial, sans-serif">(C) 2013&nbsp; <span
    style="color: rgb(0, 0, 0); font-size: medium; font-style:
    normal; font-variant: normal; font-weight: normal;
    letter-spacing: normal; line-height: normal; text-align: start;
    text-indent: 0px; text-transform: none; white-space: normal;
    word-spacing: 0px; display: inline ! important; float: none;"><span
      class="Apple-converted-space"></span>by<span
      class="Apple-converted-space">&nbsp;</span></span><a
    href="http://jasonleigh.me" style="font-size: medium;
    font-style: normal; font-variant: normal; font-weight: normal;
    letter-spacing: normal; line-height: normal; text-align: start;
    text-indent: 0px; text-transform: none; white-space: normal;
    word-spacing: 0px;">Jason Leigh</a><span style="color: rgb(0, 0,
    0); font-size: medium; font-style: normal; font-variant: normal;
    font-weight: normal; letter-spacing: normal; line-height:
    normal; text-align: start; text-indent: 0px; text-transform:
    none; white-space: normal; word-spacing: 0px; display: inline !
    important; float: none;">,<span class="Apple-converted-space">&nbsp;</span></span><a
    href="http://www.evl.uic.edu" style="font-size: medium;
    font-style: normal; font-variant: normal; font-weight: normal;
    letter-spacing: normal; line-height: normal; text-align: start;
    text-indent: 0px; text-transform: none; white-space: normal;
    word-spacing: 0px;">Electronic Visualization Laboratory</a><span
    style="color: rgb(0, 0, 0); font-size: medium; font-style:
    normal; font-variant: normal; font-weight: normal;
    letter-spacing: normal; line-height: normal; text-align: start;
    text-indent: 0px; text-transform: none; white-space: normal;
    word-spacing: 0px; display: inline ! important; float: none;">,
    University of Illinois at Chicago<br>
  </span><br>
  CAVEutil is a Python module that bundles together a number of
  useful API calls that are convenient for developing VR
  applications, which are missing in the core Omegalib library.<br>
  <br>
  There are three main classes- <a
    href="http://uic-evl.github.io/omegalib/caveutil/html/classcaveutil_1_1caveutil.html">caveutil, </a><a
    href="http://uic-evl.github.io/omegalib/caveutil/html/classcaveutil_1_1_interpol_actor.html">InterpolActor</a>.
  and <a href="http://uic-evl.github.io/omegalib/caveutil/html/classcaveutil_1_1_flipbook_actor.html">FlipbookActor</a><br>
  <br>
  CAVEUtil consists of static member functions whereas InterpolActor
  and FlipbookActor are bona fide class.<br>
  <br>
  <a href="http://uic-evl.github.io/omegalib/caveutil/html/classcaveutil_1_1caveutil.html">CAVEutil</a>
  includes a bunch of functions that condense things that normally
  take many lines of code in Omegalib to do, into single convenient
  API calls.<br>
  For example multiple lines of code for loading a scene object is
  condensed into a single <a
href="http://uic-evl.github.io/omegalib/caveutil/html/classcaveutil_1_1caveutil.html#acd861a4964d547b1f77c5573a7a117fa">loadObject()</a>
  with a bunch of input parameters.<br>
  <br>
  <a href="http://uic-evl.github.io/omegalib/caveutil/html/classcaveutil_1_1_interpol_actor.html">InterpolActor
  </a>is an Omegalib Actor to make it easier to do smooth
  interpolation of the position, orientation and scale of scene
  nodes such as 3D objects and CAVE camera. It is particularly
  convenient, for example for interpolating waypoints in the CAVE to
  create pre-recorded navigational paths.<br>
  <br>
  <a href="http://uic-evl.github.io/omegalib/caveutil/html/classcaveutil_1_1_flipbook_actor.html">FlipbookActor
  </a>is an Omegalib Actor that takes a SceneNode containing a
  number of children and cycles through them like a flipbook,
  showing only one child at a time.<br>
</font>
<h2><font face="Helvetica, Arial, sans-serif">API<br>
  </font></h2>
<h2><font face="Helvetica, Arial, sans-serif"><span style="color:
      rgb(0, 0, 0); font-size: medium; font-style: normal;
      font-variant: normal; font-weight: normal; letter-spacing:
      normal; line-height: normal; text-align: start; text-indent:
      0px; text-transform: none; white-space: normal; word-spacing:
      0px; display: inline ! important; float: none;"></span></font></h2>
<font face="Helvetica, Arial, sans-serif"><span style="color: rgb(0,
    0, 0); font-size: medium; font-style: normal; font-variant:
    normal; font-weight: normal; letter-spacing: normal;
    line-height: normal; text-align: start; text-indent: 0px;
    text-transform: none; white-space: normal; word-spacing: 0px;
    display: inline ! important; float: none;">&nbsp;&nbsp;&nbsp; <a
      href="http://uic-evl.github.io/omegalib/caveutil/html/classes.html">CAVEUtil Python API</a><br>
    <br>
  </span><span style="color: rgb(0, 0, 0); font-size: medium;
    font-style: normal; font-variant: normal; font-weight: normal;
    letter-spacing: normal; line-height: normal; text-align: start;
    text-indent: 0px; text-transform: none; white-space: normal;
    word-spacing: 0px; display: inline ! important; float: none;"></span></font>
<h2><font face="Helvetica, Arial, sans-serif">Example 1</font></h2>
<p><font face="Helvetica, Arial, sans-serif">demo.py shows how to
    use most of the CAVEutil functions as well as the InterpolActor
    class.<br>
    In particular it loads a background scene, creates a set of
    Smart Lights that automatically adjust themselves with the scale
    of the scene, and then loads in a bunch of objects that move and
    scale under interpolation. Additional CAVEutil code for getting
    and attaching objects to one's wand and head are demonstrated.<br>
  </font></p>
<img alt="" src="http://uic-evl.github.io/omegalib/caveutil/caveutil.png" height="461" width="818">
<h2><font face="Helvetica, Arial, sans-serif">Example 2</font></h2>
<p><font face="Helvetica, Arial, sans-serif">waypointdemo.py is a
    simple demo to show how to use InterpolActor to interpolate
    between CAVE waypoints<br>
  </font></p>
<p><font face="Helvetica, Arial, sans-serif">Drive around the scene
    in the CAVE and press the DOWN DPAD to record a waypoint
    location. An unlimited number of waypoints can be created.<br>
    To play back the sequence, press the UP DPAD.<br>
  </font></p>
<p><font face="Helvetica, Arial, sans-serif">Once a set of waypoints
    has been created you can save them to a file by pressing the 'd'
    key.<br>
    When you restart the program you can press the 'r' key to read
    all the waypoints back.<br>
  </font></p>
<h2><font face="Helvetica, Arial, sans-serif">Example 3<br>
  </font></h2>
<p><font face="Helvetica, Arial, sans-serif">flipbookdemo.py loads 3
    objects into the scene, a fractal, a light saber and a targeting
    cursor (i.e. the same objects used in the previous demos) and
    plays them back as if each object is a frame of an animation.
    You can control the Flipbook Actor with member functions such as
    play(), stop(), loop(), setFrameRate(), setCurrentFrame(),
    hideAllFrames(). <br>
  </font></p>
<p><font face="Helvetica, Arial, sans-serif">To play the animation
    forwards press either F or DPAD UP<br>
    To play the animation backwards press either B or DPAD DOWN<br>
    To single step to next frame press either N or DPAD RIGHT<br>
    To single step to previous frame press either P or DPAD LEFT<br>
  </font></p>
<h2 style="color: rgb(0, 0, 0); font-style: normal; font-variant:
  normal; letter-spacing: normal; line-height: normal; text-align:
  start; text-indent: 0px; text-transform: none; white-space:
  normal; word-spacing: 0px;"><font face="Helvetica, Arial,
    sans-serif">Release Notes</font></h2>
<ul style="color: rgb(0, 0, 0); font-size: medium; font-style:
  normal; font-variant: normal; font-weight: normal; letter-spacing:
  normal; line-height: normal; text-align: start; text-indent: 0px;
  text-transform: none; white-space: normal; word-spacing: 0px;">
  <li><font face="Helvetica, Arial, sans-serif"><font
        face="Helvetica, Arial, sans-serif">8/17/2013 - Added
        Flipbook Actor.</font></font></li>
  <li><font face="Helvetica, Arial, sans-serif"><font
        face="Helvetica, Arial, sans-serif">8/16/2013- Typo fix in
        waypointdemo.py and also added waypoint saving to file using
        Python's <a
          href="http://docs.python.org/2/library/pickle.html">Pickle
        </a>module.</font></font></li>
  <li><font face="Helvetica, Arial, sans-serif">8/15/2013- First
      version released.</font></li>
</ul>
<font face="Helvetica, Arial, sans-serif"><br>
</font>
