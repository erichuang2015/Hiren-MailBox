var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    entry: [
        './static/app/App.jsx'
    ],
    output : {
        path: __dirname,
        filename: './static/js/bundle.js'
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['react', 'es2015']
                }
            }
           // { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel?transform-es2015-arrow-functions'}
        ]
    },

    plugins: process.env.NODE_ENV === 'production' ? [
        new webpack.optimize.DedupePlugin(),
        new webpack.optimize.OccurrenceOrderPlugin(),
        new webpack.optimize.UglifyJsPlugin()
    ] : [new BundleTracker({filename: './webpack-stats.json'})],
};
