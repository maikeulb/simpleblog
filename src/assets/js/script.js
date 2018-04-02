import 'semantic-ui-css/semantic.min.css';
import 'semantic-ui-css/semantic.min.js';

window.$ = window.jQuery = require('jquery');

$(document)
  .ready(function() {
    // fix main menu to page on passing
    $('.main.menu').visibility({
      type: 'fixed'
    });
    $('.overlay').visibility({
      type: 'fixed',
      offset: 80
    });
    // lazy load images
    $('.image').visibility({
      type: 'image',
      transition: 'vertical flip in',
      duration: 500
    });
    // show dropdown on hover
    $('.main.menu  .ui.dropdown').dropdown({
      on: 'hover'
    });
  })
;

import '../css/styles.scss';

import logoSmall from '../images/logo.png';
var logoImg = document.getElementById('logo_sm');
logoImg.src = logoSmall;
