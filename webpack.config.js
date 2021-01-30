const path = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack')
const BundleTrcker = require('webpack-bundle-tracker')

module.exports = {
    context: __dirname,
    entry: {
        'main': './assets/js/index'
    }, // entry point of our app

    output: {
        path: path.resolve('./assets/bundles'),
        publicPath: "/static/bundles/",
        filename: "[name]-[hash].js"
    },

    plugins: [
        new BundleTrcker({
            path: __dirname,
            filename: './webpack-stats.json'
        }),
        new MiniCssExtractPlugin(),
    ],

    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel-loader'
            },
            {
                    test: /\.css$/,
                    use: [
                        MiniCssExtractPlugin.loader,
                        'css-loader',
                    ]
            }
        ]

    }
}