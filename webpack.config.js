var path = require('path');
var webpack = require("webpack");
var mainPath = path.resolve(__dirname, 'src', 'main.js');
var outputPath = path.resolve(__dirname, 'dist');

module.exports = {
    devtool: 'cheap-module-eval-source-map',
    devServer: {
        inline: true,
        contentBase: [
            path.join(__dirname, "static")
        ],
        compress: false
    },
    entry: [
        mainPath
    ],
    output: {
        filename: "dist/baseinit.js",
    },
    resolve: {
        extensions: ['.js', '.vue', '.json'],
        alias: {
            'vue$': 'vue/dist/vue.esm.js',
            '@': path.resolve('src'),
        }
    },
    module: {
        rules:[
            {
                test: /\.vue$/,
                use: [{
                    loader: 'vue-loader',
                    // options: {
                    //     loaders: {
                    //         js: 'babel-loader!eslint-loader'
                    //     }
                    // }
                }]
            },
            {
                test: /\.js$/,
                exclude: [/node_modules/],
                use: [{
                  loader: 'babel-loader',
                //   options: { presets: ['es2015'] }
                }]
            },
            {
                test: /\.css$/,
                use: ['style-loader', {
                    loader: 'css-loader',
                    options: { modules: true }
                }]
            },
            {
                test: /\.(sass|scss)$/,
                use: [
                    'style-loader',
                    'css-loader',
                    'sass-loader',
                ]
            }
        ]
    }
}