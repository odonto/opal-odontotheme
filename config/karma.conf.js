module.exports = function(config){
  var opalPath = process.env.OPAL_LOCATION;
  var karmaDefaults = require(opalPath + '/opal/tests/js_config/karma_defaults.js');
  var baseDir = __dirname + '/..';
  var coverageFiles = [
    __dirname+'/../odontotheme/static/js/odontotheme/**/*.js',
  ];
    var includedFiles = [
      __dirname+'/../odontotheme/static/js/odontotheme/**/*.js',
      __dirname+'/../odontotheme/static/js/test/*.js',
  ];

  var defaultConfig = karmaDefaults(includedFiles, baseDir, coverageFiles);
  config.set(defaultConfig);
};