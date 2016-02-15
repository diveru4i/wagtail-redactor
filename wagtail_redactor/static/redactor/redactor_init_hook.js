/* global jQuery */
(function ($) {
    $(function () {
        var $document = $(document);

        $document.on('click', 'button[class*="icon-redactor"], button[class*="icon-plus"]', function () {
            var $redactors = $('textarea.redactor-box');
            if ($redactors.length) {
                $redactors.each(function () {
                    var $redactor = $(this);
                    if (!$redactor.is('.hook-done')) {
                        var event = $.Event('redactor:init');
                        event.target = $redactor.get(0);
                        $document.trigger(event);
                        $redactor.addClass('hook-done');
                    }
                });
            }
        });
    });
}(jQuery));
