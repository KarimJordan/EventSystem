const webpack = require("webpack")
const path = require("path")
const ExtractTextPlugin = require("extract-text-webpack-plugin")
const MinCssExtractPlugin = require("mini-css-extract-plugin")
const VueLoaderPlugin = require('vue-loader/lib/plugin')

const entry = {
    core: path.resolve('./core/js/main.js'),
    event: path.resolve('./event/js/main.js')
}

const output = {
    path: __dirname,
    filename: "./[name]/static/compiled/js/[name].js"
}

const modules = {
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
}

const resolve = {
    extensions: ['.js', '.vue'],
    alias: {
        'vue': 'vue/dist/vue.common.js'
    },
}

module.exports = {
    entry: entry,
    output: output,
    plugins: [
        new VueLoaderPlugin(),
        new MinCssExtractPlugin({
            filename: "./[name]/static/compiled/css/[name].css",
            chunkFilename: "./[id]/static/compiled/css/[id].css"
        })
    ],
    module: modules,
    resolve: resolve
}