const webpack = require("webpack")
const path = require("path")
const ExtractTextPlugin = require("extract-text-webpack-plugin")
const MinCssExtractPlugin = require("mini-css-extract-plugin")
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
    entry: {
        core: path.resolve('./core/js/main.js'),
        event: path.resolve('./event/js/main.js')
    },

    // compiled bundled location
    output: {
        path: __dirname,
        filename: "./[name]/static/compiled/js/[name].js"
    },

    plugins: [
        new VueLoaderPlugin(),
        new MinCssExtractPlugin({
            filename: "./[name]/static/compiled/css/[name].css",
            chunkFilename: "./[id]/static/compiled/css/[id].css"
        })
    ],

    // contains loaders,
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    MinCssExtractPlugin.loader,
                    "css-loader"
                ]
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                }
            }
        ],
    },

    resolve: {
        extensions: ['.js', '.vue'],
        alias: {
            'vue': 'vue/dist/vue.common.js'
        },
    }
}