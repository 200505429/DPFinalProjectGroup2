$(function(){
    function pageLoad(){
        nv.addGraph(function() {
            var chart = nv.models.lineChart()
                .useInteractiveGuideline(true)
                .margin({top: 0, bottom: 25, left: 25, right: 0})
                //.showLegend(false)
                .color([
                    '#6294c9', '#59bc79'
                ]);

            chart.legend.margin({top: 3});

            chart.yAxis
                .showMaxMin(false)
                .tickFormat(d3.format(',.f'));
			
			
            var data = '[{"key":"Wind","values":[{"x":1,"y":44},{"x":2,"y":32},{"x":3,"y":14},{"x":4,"y":12},{"x":5,"y":13},{"x":6,"y":15},{"x":7,"y":14},{"x":8,"y":16},{"x":9,"y":15},{"x":10,"y":19},{"x":11,"y":17},{"x":12,"y":12},{"x":13,"y":14},{"x":14,"y":15},{"x":15,"y":12},{"x":16,"y":11},{"x":17,"y":13},{"x":18,"y":14},{"x":19,"y":13},{"x":20,"y":12},{"x":21,"y":18},{"x":22,"y":15},{"x":23,"y":19},{"x":24,"y":28},{"x":25,"y":42},{"x":26,"y":87},{"x":27,"y":152},{"x":28,"y":234},{"x":29,"y":296},{"x":30,"y":327}]},{"key":"Temperature","values":[{"x":1,"y":44},{"x":2,"y":32},{"x":3,"y":14},{"x":4,"y":12},{"x":5,"y":13},{"x":6,"y":15},{"x":7,"y":14},{"x":8,"y":16},{"x":9,"y":15},{"x":10,"y":19},{"x":11,"y":17},{"x":12,"y":12},{"x":13,"y":14},{"x":14,"y":15},{"x":15,"y":12},{"x":16,"y":11},{"x":17,"y":13},{"x":18,"y":14},{"x":19,"y":13},{"x":20,"y":12},{"x":21,"y":18},{"x":22,"y":15},{"x":23,"y":19},{"x":24,"y":28},{"x":25,"y":42},{"x":26,"y":87},{"x":27,"y":152},{"x":28,"y":234},{"x":29,"y":296},{"x":30,"y":327}]}]';
			
			data=JSON.parse(data);
			
            data[0].area = true;
            d3.select('#visits-chart svg')
                .datum(data)
                .transition().duration(500)
                .call(chart);

            PjaxApp.onResize(chart.update);

            return chart;
        });

        /* Sparklines can also take their values from the first argument
         passed to the sparkline() function */
        function randomValue(){
            return Math.floor( Math.random() * 40 );
        }
        var values = [[],[],[],[],[]],
            options = {
                width: '150px',
                height: '30px',
                lineColor: $white,
                lineWidth: '2',
                spotRadius: '2',
                highlightLineColor: $gray,
                highlightSpotColor: $gray,
                spotColor: false,
                minSpotColor: false,
                maxSpotColor: false
            };
        for (var i = 0; i < values.length; i++){
            values[i] = [10 + randomValue(), 15 + randomValue(), 20 + randomValue(), 15 + randomValue(), 25 + randomValue(),
                25 + randomValue(), 30 + randomValue(), 30 + randomValue(), 40 + randomValue()]
        }

        function drawSparkLines(){
            options.lineColor = $green;
            options.fillColor = 'rgba(86, 188, 118, 0.1)';
            $('#direct-trend').sparkline(values[0], options );
            options.lineColor = $orange;
            options.fillColor = 'rgba(234, 200, 94, 0.1)';
            $('#refer-trend').sparkline(values[1], options );
            options.lineColor = $blue;
            options.fillColor = 'rgba(106, 141, 167, 0.1)';
            $('#social-trend').sparkline(values[2], options );
            options.lineColor = $red;
            options.fillColor = 'rgba(229, 96, 59, 0.1)';
            $('#search-trend').sparkline(values[3], options );
            options.lineColor = $white;
            options.fillColor = 'rgba(255, 255, 255, 0.1)';
            $('#internal-trend').sparkline(values[4], options );
        }

        drawSparkLines();

        PjaxApp.onResize(drawSparkLines);


        // Notification link click handler.
        // JUST FOR DEMO.
        // Can be removed.

        function close(e){
            var $settings = $("#settings"),
                $popover = $settings.siblings(".popover");
            if($popover.length && !$.contains($popover[0], e.target)){
                $settings.popover('hide');
                $(document).off("click", close);
            }
        }
        $("#notification-link").click(function(){
            if ( $(window).width() > 767){
                $("#settings").popover('show');
                $(document).on("click", close);
                return false;
            }
        });

        $("#feed").slimscroll({
            height: 'auto',
            size: '5px',
            alwaysVisible: true,
            railVisible: true
        });

        $("#chat-messages").slimscroll({
            height: '240px',
            size: '5px',
            alwaysVisible: true,
            railVisible: true
        });

        $('.widget').widgster();
    }

    pageLoad();

    PjaxApp.onPageLoad(pageLoad);
});

