import React from "react";
import ReactDOM from "react-dom";
import swal from "sweetalert2";
import "regenerator-runtime/runtime";
import BootstrapTable from 'react-bootstrap-table-next';
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';


class Sent extends React.Component {
    constructor(prop) {
        super(prop);
        this.products = [
            {"id": 1, "name": "Xxx", "price": "521$", "date": ""},
            {"id": 2, "name": "444", "price": "421$", "date": "sss"},
        ];
        this.columns = [{
            dataField: 'id',
            text: 'From'
        }, {
            dataField: 'name',
            text: 'To'
        }, {
            dataField: 'price',
            text: 'Subject'
        },
            {
                dataField: "date",
                text: "Date"
            }];
        this.state = {
            from: "",
            to: "",
            cc: [],
            bcc: [],
            subject: "",
            body: "",
            attachment: ""
        }
    }

    componentDidMount() {

    }

    render() {
        return(
            <BootstrapTable keyField='id' data={ this.products } columns={ this.columns } />
        )
    }

}

ReactDOM.render(<Sent />, document.getElementById("sent"));