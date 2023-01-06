/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.HtPartner = publicWidget.Widget.extend({
    selector: '.display-partner',
    start() {
        let partnersRow = this.el.querySelector('#ht-partner-row')
        console.log("ici")
        if (partnersRow){
            this._rpc({
                route: '/partners/',
                params:{}
            }).then(data=>{
                let html = ``
                data.forEach(partner=>{
                    html += `<div class="col-lg-3 mb-5">
                        <div class="d-flex align-items-center">
                            <div class="img-container ">
                                <a href=" ${partner.url}">
                                    <img class="partner-image rounded" src="data:image/png;base64,${partner.image}" />
                              </a>
                            </div>

                        </div>


                    </div>`
                })
                partnersRow.innerHTML = html
            })
        }else{
            console.log("coucou")
        }
    },
});

export default publicWidget.registry.HtPartner;

