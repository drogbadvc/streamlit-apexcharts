import React from "react"
import Chart from "react-apexcharts";
import deepMap from "./utils"

import {
    StreamlitComponentBase,
    withStreamlitConnection
} from "streamlit-component-lib";

interface ApexArgs {
    options: any;
    series: any[];
    types?: "line"
        | "area"
        | "bar"
        | "histogram"
        | "pie"
        | "donut"
        | "radialBar"
        | "scatter"
        | "bubble"
        | "heatmap"
        | "treemap"
        | "boxPlot"
        | "candlestick"
        | "radar"
        | "polarArea"
        | "rangeBar";
    width?: string | number,
}

export class App extends StreamlitComponentBase {
    render() {
        const JS_PLACEHOLDER = "--x_x--0_0--"
        const evalStringToFunction = (s: string) => {
            let funcReg = new RegExp(
                `${JS_PLACEHOLDER}\\s*(function\\s*.*)\\s*${JS_PLACEHOLDER}`
            )
            let match = funcReg.exec(s)
            if (match) {
                const funcStr = match[1]
                return new Function("return " + funcStr)()
            } else {
                return s
            }
        }
        /**
         * Deep map all values in an object to evaluate all strings as functions
         * @param obj object to deep map on
         * @returns object with all functions in values evaluated
         */
        const evalStringToFunctionDeepMap = (obj: object) => {
            return deepMap(obj, evalStringToFunction, {})
        }
        const {options, series, types, width}: ApexArgs = this.props.args
        const cleanOptions = evalStringToFunctionDeepMap(options)

        return (
            <div className="card">
                <div className="card-body">
                    <h5 className="card-title"></h5>
                    <div className="app">
                        <div className="row">
                            <div className="mixed-chart">
                                <Chart
                                    options={cleanOptions}
                                    series={series}
                                    type={types}
                                    width={width}
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default withStreamlitConnection(App);