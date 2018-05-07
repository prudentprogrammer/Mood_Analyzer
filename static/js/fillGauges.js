d3.queue()
  .defer(d3.json, "static/mockresponses/emotion_response.json") //our data for the bar chart
  .await(loadEmotions); //ready is the function name

function loadEmotions(error, data) {
    if (isNaN(data.sentiment.document.score)) {
        score = 50;
    }
    var score = 0;
    if (data.sentiment.document.score) {
    //POSITIVE ( no neg cuz it encourages positivity )
        if (data.sentiment.document.score< 0) {
            score = 1 + Number(data.sentiment.document.score);
        } else {
            score = data.sentiment.document.score;
        }
    }
    console.log(data);
    console.log(score);
    var gauge1 = loadLiquidFillGauge("fillgauge1", score * 100);
    //ANGER
    var config1 = liquidFillGaugeDefaultSettings();
    config1.circleColor = "#d8280b";
    config1.textColor = "#FF4444";
    config1.waveTextColor = "#FFAAAA";
    config1.waveColor = "#FFDDDD";
    config1.circleThickness = 0.2;
    config1.textVertPosition = 0.2;
    config1.waveAnimateTime = 3000;
    var gauge2 = loadLiquidFillGauge("fillgauge2", data.emotion.document.emotion.anger * 100, config1);


    //FEAR
    var config2 = liquidFillGaugeDefaultSettings();
    config2.circleColor = "#7109d6";
    config2.textColor = "#460882";
    config2.waveTextColor = "#460882";
    config2.waveColor = "#b06fef";
    config2.circleThickness = 0.2;
    config2.textVertPosition = 0.2;
    config2.waveAnimateTime = 3000;
    var gauge3 = loadLiquidFillGauge("fillgauge3", data.emotion.document.emotion.fear * 100, config2);

    //DISGUST
    var config3 = liquidFillGaugeDefaultSettings();
    config3.circleColor = "#37a30a";
    config3.textColor = "#266d09";
    config3.waveTextColor = "#266d09";
    config3.waveColor = "#c6f9a5";
    config3.circleThickness = 0.2;
    config3.textVertPosition = 0.2;
    config3.waveAnimateTime = 3000;
    var gauge4 = loadLiquidFillGauge("fillgauge4", data.emotion.document.emotion.disgust * 100, config3);
    var config4 = liquidFillGaugeDefaultSettings();


    //JOY
    config4.circleColor = "#ce970d";
    config4.textColor = "#d68816";
    config4.waveTextColor = "#d68816";
    config4.waveColor = "#edc370";
    config4.circleThickness = 0.2;
    config4.textVertPosition = 0.2;
    config4.waveAnimateTime = 3000;
    var gauge5 = loadLiquidFillGauge("fillgauge5", data.emotion.document.emotion.joy * 100, config4);
    var config5 = liquidFillGaugeDefaultSettings();


    //SADNESS
    config5.circleColor = "#4433e5";
    config5.textColor = "#1a09b5";
    config5.waveTextColor = "#1a09b5";
    config5.waveColor = "#71acf4";
    config5.circleThickness = 0.2;
    config5.textVertPosition = 0.2;
    config5.waveAnimateTime = 3000;
    config5.displayPercent = false;
    var gauge6 = loadLiquidFillGauge("fillgauge6",
        data.emotion.document.emotion.sadness * 100, config5);

    function NewValue() {
        if (Math.random() > .5) {
            return Math.round(Math.random() * 100);
        } else {
            return (Math.random() * 100).toFixed(1);
        }
    }
  };