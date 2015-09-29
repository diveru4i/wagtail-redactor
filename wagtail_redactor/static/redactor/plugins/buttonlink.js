if (!RedactorPlugins) var RedactorPlugins = {};

RedactorPlugins.buttonlink = function()
{
    return {
        init: function(v)
        {
            var button = this.button.add('buttonlink', 'Сделать ссылку кнопкой');
            this.button.setAwesome('buttonlink', 'fa-bullseye');
            this.button.addCallback(button, this.buttonlink.show);
        },
        show: function()
        {
            var link = this.selection.getNodes()[0];
            var node = $('<p class="button_block"></p>');
            $(link).addClass('button');
            $(link).wrap(node);
            this.code.sync();
        },
    };
};