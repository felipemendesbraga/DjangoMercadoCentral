// the semi-colon before function invocation is a safety net against concatenated
// scripts and/or other plugins which may not be closed properly.
;( function( $, window, document, undefined ) {

    "use strict";

    var pluginName = 'djangoInputMask';

    function Plugin(container, options) {
        this.container = container;
        this.init();
    }

    $.extend(Plugin.prototype, {
        init: function() {
            $(this.container).find('[data-input-mask]').each(this.initInputMask);
            $(this.container).find('[data-money-mask]').each(this.initMoneyMask);
        },

        initInputMask: function() {
            var input = $(this),
                opts = input.attr('data-input-mask').replace(/&quot;/g, '"'),
                opts = JSON.parse(opts),
                mask = opts.mask;

            opts.placeholder = input.attr('placeholder');

            // maxlength causes a bug in jquery-maskedinput in android
            input.removeAttr('maxlength');


            input.mask(mask.mask, opts);
        },

        initMoneyMask: function() {
            var input = $(this),
                opts = input.attr('data-money-mask').replace(/&quot;/g, '"'),
                opts = JSON.parse(opts);

            input.maskMoney(opts);

            if (opts.allowZero || input.val() != '') {
                input.maskMoney('mask');
            }
        }
    });

    $.fn[pluginName] = function(options) {
        return this.each(function(){
            new Plugin(this, options);
        });
    };

} )( jQuery, window, document );


$(function(){
    $('body').djangoInputMask();
    $('body').bind('DOMNodeInserted', '[data-input-mask]', function () {
        $('body').djangoInputMask();
    });

});
