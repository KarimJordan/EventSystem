const webpack = require("webpack")
const path = require("path")
const ExtractTextPlugin = require("extract-text-webpack-plugin")

module.exports = {
    entry : {
        event: path.resolve('./event/js/main.js')
    },

    // compiled bundled location
    output: {
        path: __dirname,
        filename: "./[name]/static/compiled/js/[name].js"
    },

    // contains loaders,
    module: {
        loaders: [
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    use: ['css-loader', 'style-loader']
                })
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader',
            }
        ]
    },

    resolve: {
        extensions: ['.js', '.vue'],
        alias: {
            'vue': 'vue/dist/vue.common.js'
        },
        // alias: {'vue$': 'vue/dist/vue.esm.js'},
        // extensions: ['.js', '.vue'], // this string resolve your problem
    }
}