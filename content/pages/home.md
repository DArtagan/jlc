Title: Homepage
Date: 2015-02-27 10:42
save_as: index.html

<div class="banner" data-parallax="scroll" data-image-src="/assets/images/fall_2.jpg">
<div class="quote">
  <blockquote><h2>When you can't see the forest for the trees</h2> <p>-- You are so caught up with the details of a problem you are unable see the situation as a whole.</p></blockquote>
</div>
</div>

<div class="container" markdown="1">
<div class="section_light" markdown="1">

Welcome to my website.  I am a licensed psychotherapist, with a private practice in Wheat Ridge, Colorado.  I work primarily with adults.  If you are struggling with anxiety, depressionn, addiction, trauma, PTSD, sexual or physical abuse, relationship issues, grief and loss, you have come to the right place.  As a therapist, I work top empower you to address your issues and make the necessary changes.  Together, we focus our awareness on the things that are not working for you at this time in your life.  Therapy is a process of exploration and problem soving to create the desired change.  

My interpersonal style is based on creating an open, safe space for clients inner exploration and growth.  I provide a supportive and respectful atmosphere for you to examine your thougts, feelings, beliefs and behaviours by incorporating various professional techniques.  You and I will choose the approach that best fits your needs.

</div>
</div>

<div class="quote" data-parallax="scroll" data-image-src="/assets/images/fall_1.jpg">
<blockquote class="blockquote-reverse">Happiness is when what you think, what you say, and what you do are in harmony. <footer>Mohandas Gandhi</footer></blockquote>
</div>

<div markdown="1">
<div class="container" markdown="1">
<div class="section_light" markdown="1">

## About

I am a licensed professional counselor and have been working in the mental health field for over 10 years.  My approach is grounded in Rational Emotive Behavioural Theory which seeks to identify and eliminate irrational beliefs that may cause maladaptive behavior.  I also integrate EMDR (Eye Movement Desensitization and Reprocessing) into my practice along with an array of other eclectic theories.  

I hold a Master's degree in Community Counseling from the University of Northern Colorado.  I am a Certified Addictions Counselor level three, and EMDR trained, level two.  

</div>
</div>
</div>

<div class="quote" data-parallax="scroll" data-image-src="/assets/images/fall_2.jpg">
<blockquote class="blockquote-reverse">The universe is change, our life is what our thoughts make it."<footer>Marcus Aurelius Antoninus</footer></blockquote>
</div>

<div class="container-fullwidth">
  <div class="map-overlay" onClick="style.pointerEvents='none'"></div>
  <div id="contact-map" class="col-md-6"></div>
</div>

<div class="container" markdown="1">
<div class="section_light" markdown="1">

## Contact

Janet L. Couts, L.P.C., C.A.C. III

<address>
    5810 West 38th Avenue<br />
    Suite 8<br />
    Wheat Ridge, 80212
</address>

<address>
    Phone: 303.359.8036<br />
    Fax: 303.456.9284<br />
    Email: couttsj@live.com
</address>

Hours: Monday through Thursday 11:00am - 6:00pm

Fees: 100.00 a session (50 minutes)

Insurances accepted: Cigna/AETNA/Blue Cross Blue Shield/Cofinity/Cover Colorado/Beech Street/Corp Health/Anthem Blue Cross/Victims Comp/Mines and Associates.

I also work with insurances as an out-of-network provider.
Individuals are requested to pay at the time services are rendered and a receipt will be offered so individual may request reimbursement from their insurance company.

</div>
</div>


<script src="//maps.google.com/maps/api/js?sensor=false"></script>
<script>	
  function init_map() {
    var var_location = new google.maps.LatLng(39.76898,-105.06117);

    var var_mapoptions = {
        center: var_location,
        zoom: 14 
    };

    var var_marker = new google.maps.Marker({
        position: var_location,
        map: var_map,
        title:"JLC Counseling"});

    var var_map = new google.maps.Map(document.getElementById("contact-map"),
        var_mapoptions);

    var_marker.setMap(var_map);	

  }

  google.maps.event.addDomListener(window, 'load', init_map);
</script>
